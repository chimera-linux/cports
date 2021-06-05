from cbuild.core import logger

import os

class GnuLike:
    def __init__(self, tmpl, cexec, default_flags, default_ldflags):
        self.template = tmpl
        self.cexec = cexec
        self.flags = default_flags
        self.ldflags = default_ldflags

    def invoke(
        self, inputs, output, obj_file = False, flags = [], ldflags = []
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
        if not obj_file:
            argsbase += ldflags
            # to compile an object file
            argsbase.append("-c")
        # output always
        argsbase += ["-o", os.path.join(pkg.chroot_build_wrksrc, output)]
        # fire
        logger.get().out_plain(self.cexec + " " + " ".join(argsbase))
        return self.template.do(self.cexec, argsbase, build = True)

class C(GnuLike):
    def __init__(self, tmpl, cexec = "cc"):
        super().__init__(tmpl, cexec, tmpl.CFLAGS, tmpl.LDFLAGS)

class CXX(GnuLike):
    def __init__(self, tmpl, cexec = "cxx"):
        super().__init__(tmpl, cexec, tmpl.CXXFLAGS, tmpl.LDFLAGS)
