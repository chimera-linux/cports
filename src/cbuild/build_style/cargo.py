from cbuild.util import cargo


def do_prepare(self):
    self.cargo.vendor()
    cargo.setup_vendor(self)


def do_build(self):
    self.cargo.build()


def do_check(self):
    self.cargo.check()


def do_install(self):
    self.cargo.install()


def use(tmpl):
    tmpl.do_prepare = do_prepare
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.cargo = cargo.Cargo(tmpl)
