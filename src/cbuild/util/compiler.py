from cbuild.core import logger
import shlex


def _get_lld_cpuargs(lthreads):
    return [
        # lld does not gain any non-lto benefit past 16, and is only slower
        f"--threads={min(lthreads, 16)}",
        f"--thinlto-jobs={lthreads}",
    ]


class GnuLike:
    def __init__(self, tmpl, cexec, default_flags, default_ldflags):
        self.template = tmpl
        self.cexec = cexec
        self.flags = default_flags
        self.ldflags = default_ldflags

    def invoke(
        self, inputs, output, obj_file=False, flags=[], ldflags=[], quiet=False
    ):
        pkg = self.template
        # default flags + inputs are always passed
        argsbase = self.flags + list(map(lambda v: str(v), inputs))
        # default linker flags if linking an executable
        if not obj_file:
            argsbase += self.ldflags
        # custom flags always
        argsbase += flags
        # custom ldflags sometimes
        if obj_file:
            # to compile an object file
            argsbase.append("-c")
        else:
            argsbase += ldflags
        # output always
        argsbase += ["-o", str(pkg.chroot_cwd / output)]
        # fire
        if not quiet:
            logger.get().out_plain(
                self.cexec + " " + shlex.join(map(lambda v: str(v), argsbase))
            )
        return self.template.do(self.cexec, *argsbase)


class C(GnuLike):
    def __init__(self, tmpl, cexec=None):
        if not cexec:
            cexec = tmpl.get_tool("CC")
        super().__init__(tmpl, cexec, tmpl.get_cflags(), tmpl.get_ldflags())


class CXX(GnuLike):
    def __init__(self, tmpl, cexec=None):
        if not cexec:
            cexec = tmpl.get_tool("CXX")
        super().__init__(tmpl, cexec, tmpl.get_cxxflags(), tmpl.get_ldflags())
