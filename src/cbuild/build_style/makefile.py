from cbuild.util import make
import shlex

def do_build(self):
    if self.make_use_env:
        self.make.build()
        return

    # by default, pass various stuff directly rather than through env
    tool_args = [
        "PREFIX=/usr",
        "OBJCOPY=" + self.get_tool("OBJCOPY"),
        "RANLIB=" + self.get_tool("RANLIB"),
        "CXX=" + self.get_tool("CXX"),
        "CPP=" + self.get_tool("CPP"),
        "CC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("LD"),
        "AR=" + self.get_tool("AR"),
        "AS=" + self.get_tool("AS"),
        "CFLAGS=" + self.get_cflags(shell = True),
        "FFLAGS=" + self.get_fflags(shell = True),
        "LDFLAGS=" + self.get_ldflags(shell = True),
        "CXXFLAGS=" + self.get_cxxflags(shell = True),
    ]

    if not self.bootstrapping:
        tool_args.append("OBJDUMP=" + self.get_tool("OBJDUMP"))

    self.make.build(tool_args)

def do_check(self):
    self.make.check()

def do_install(self):
    self.make.install(["STRIP=true", "PREFIX=/usr"])

def use(tmpl):
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.make = make.Make(tmpl)
