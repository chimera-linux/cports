from cbuild.util import golang


def prepare(self):
    self.golang.mod_download()


def build(self):
    self.golang.build()


def check(self):
    self.golang.check()


def install(self):
    self.golang.install()


def use(tmpl):
    tmpl.prepare = prepare
    tmpl.build = build
    tmpl.check = check
    tmpl.install = install

    tmpl.golang = golang.Golang(tmpl)

    tmpl.build_style_defaults = [
        ("make_dir", "build"),
    ]
