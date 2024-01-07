from cbuild.util import make


def do_configure(self):
    self.do(
        self.chroot_cwd / self.configure_script,
        *self.configure_args,
        wrksrc=self.make_dir,
    )


def do_build(self):
    self.make.build()


def do_check(self):
    self.make.check()


def do_install(self):
    self.make.install()


def use(tmpl):
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.make = make.Make(tmpl)
