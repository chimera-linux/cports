from cbuild.util import cargo


def prepare(self):
    self.cargo.vendor()


def build(self):
    self.cargo.build()


def check(self):
    self.cargo.check()


def install(self):
    self.cargo.install()


def use(tmpl):
    tmpl.prepare = prepare
    tmpl.build = build
    tmpl.check = check
    tmpl.install = install

    tmpl.cargo = cargo.Cargo(tmpl)
