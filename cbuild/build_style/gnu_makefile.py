from cbuild.util import make

def do_build(self):
    self.make = make.Make(self)
    self.make.build()

def do_check(self):
    pass

def do_install(self):
    self.make.install(["STRIP=true", "PREFIX=/usr"])

def use(tmpl):
    tmpl.build_style = "gnu_makefile"
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install
