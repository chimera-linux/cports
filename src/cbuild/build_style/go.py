from cbuild.util import golang

def do_prepare(self):
    self.golang.mod_download()

def do_build(self):
    self.golang.build()

def do_check(self):
    self.golang.check()

def do_install(self):
    self.golang.install()

def use(tmpl):
    tmpl.do_prepare = do_prepare
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.golang = golang.Golang(tmpl)

    tmpl.build_style_defaults = [
        ("make_dir", "build"),
    ]
