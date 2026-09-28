from cbuild.util import make


def configure(self):
    self.do(
        self.chroot_cwd / self.configure_script,
        *self.configure_args,
        wrksrc=self.make_dir,
        env=self.configure_env,
    )


def build(self):
    self.make.build()


def check(self):
    self.make.check()


def install(self):
    self.make.install()


def use(tmpl):
    tmpl.configure = configure
    tmpl.build = build
    tmpl.check = check
    tmpl.install = install

    tmpl.make = make.Make(tmpl)
