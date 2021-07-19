from cbuild.core import logger
import shlex

class GnuLike:
    def __init__(self, tmpl, cexec, default_flags, default_ldflags):
        self.template = tmpl
        self.cexec = cexec
        self.flags = default_flags
        self.ldflags = default_ldflags

    def invoke(
        self, inputs, output, obj_file = False, flags = [], ldflags = [],
        quiet = False
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
        argsbase += ["-o", str(pkg.chroot_build_wrksrc / output)]
        # fire
        if not quiet:
            logger.get().out_plain(self.cexec + " " + shlex.join(argsbase))
        return self.template.do(self.cexec, argsbase, build = True)

class C(GnuLike):
    def __init__(self, tmpl, cexec = None):
        if not cexec:
            if tmpl.cross_build and not tmpl.build_profile.cross:
                cexec = tmpl.tools["BUILD_CC"]
            else:
                cexec = tmpl.tools["CC"]
        super().__init__(tmpl, cexec, tmpl.get_cflags(), tmpl.get_ldflags())

class CXX(GnuLike):
    def __init__(self, tmpl, cexec = None):
        if not cexec:
            if tmpl.cross_build and not tmpl.build_profile.cross:
                cexec = tmpl.tools["BUILD_CXX"]
            else:
                cexec = tmpl.tools["CXX"]
        super().__init__(tmpl, cexec, tmpl.get_cxxflags(), tmpl.get_ldflags())
