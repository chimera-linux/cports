from cbuild.util import meson


def configure(self):
    meson.configure(
        self,
        self.make_dir,
        self.meson_dir,
        self.configure_args,
        self.configure_env,
    )


def build(self):
    renv = dict(self.make_env)
    renv.update(self.make_build_env)
    eargs = []
    if self.verbose:
        eargs += ["--verbose"]
    self.do(
        *self.make_wrapper,
        *self.make_build_wrapper,
        self.make_cmd,
        "-j",
        str(self.make_jobs),
        *eargs,
        self.make_build_target,
        *self.make_build_args,
        "meson-test-prereq",
        wrksrc=self.make_dir,
        env=renv,
    )


def check(self):
    renv = dict(self.make_env)
    renv.update(self.make_check_env)
    meson.test(
        self,
        self.make_dir,
        self.make_check_args,
        renv,
        self.make_wrapper + self.make_check_wrapper,
    )


def install(self):
    renv = dict(self.make_env)
    renv.update(self.make_install_env)
    meson.install(
        self,
        self.make_dir,
        self.make_install_args,
        renv,
        self.make_wrapper + self.make_install_wrapper,
    )


def use(tmpl):
    tmpl.configure = configure
    tmpl.build = build
    tmpl.check = check
    tmpl.install = install

    tmpl.build_style_defaults = [
        ("make_build_target", "all"),
        ("make_dir", "build"),
        ("make_cmd", "ninja"),
    ]
