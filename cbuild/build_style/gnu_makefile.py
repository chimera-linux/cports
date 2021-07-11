from cbuild.util import make
import shlex

def do_build(self):
    if self.make_use_env:
        self.make.build()
        return

    # by default, pass various stuff directly rather than through env
    self.make.build([
        "OBJCOPY=" + self.tools["OBJCOPY"],
        "OBJDUMP=" + self.tools["OBJDUMP"],
        "RANLIB=" + self.tools["RANLIB"],
        "CXX=" + self.tools["CXX"],
        "CPP=" + self.tools["CPP"],
        "CC=" + self.tools["CC"],
        "LD=" + self.tools["LD"],
        "AR=" + self.tools["AR"],
        "AS=" + self.tools["AS"],
        "CFLAGS=" + shlex.join(self.CFLAGS),
        "LDFLAGS=" + shlex.join(self.LDFLAGS),
        "CXXFLAGS=" + shlex.join(self.CXXFLAGS),
    ])

def do_check(self):
    pass

def do_install(self):
    self.make.install(["STRIP=true", "PREFIX=/usr"])

def use(tmpl):
    tmpl.build_style = "gnu_makefile"
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.make = make.Make(tmpl)

    tmpl.build_style_fields = [
        ("make_use_env", False, bool, False, False, False)
    ]
