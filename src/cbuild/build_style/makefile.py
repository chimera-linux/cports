from cbuild.util import make


def build(self):
    if self.make_use_env:
        self.make.build()
        return

    # by default, pass various stuff directly rather than through env
    tool_args = [
        "PREFIX=/usr",
        "PKG_CONFIG=" + self.get_tool("PKG_CONFIG"),
        "OBJCOPY=" + self.get_tool("OBJCOPY"),
        "READELF=" + self.get_tool("READELF"),
        "RANLIB=" + self.get_tool("RANLIB"),
        "CXX=" + self.get_tool("CXX"),
        "CPP=" + self.get_tool("CPP"),
        "CC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("LD"),
        "AR=" + self.get_tool("AR"),
        "AS=" + self.get_tool("AS"),
        "NM=" + self.get_tool("NM"),
        "CFLAGS=" + self.get_cflags(shell=True),
        "FFLAGS=" + self.get_fflags(shell=True),
        "LDFLAGS=" + self.get_ldflags(shell=True),
        "CXXFLAGS=" + self.get_cxxflags(shell=True),
    ]

    if self.stage > 0:
        tool_args.append("OBJDUMP=" + self.get_tool("OBJDUMP"))

    self.make.build(tool_args)


def check(self):
    self.make.check()


def install(self):
    self.make.install(["STRIP=true", "PREFIX=/usr"])


def use(tmpl):
    tmpl.build = build
    tmpl.check = check
    tmpl.install = install

    tmpl.make = make.Make(tmpl)
