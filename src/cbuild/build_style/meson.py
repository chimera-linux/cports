from cbuild.util import meson


def do_configure(self):
    meson.configure(
        self,
        self.make_dir,
        self.meson_dir,
        self.configure_args,
        self.configure_env,
    )


def do_build(self):
    renv = dict(self.make_env)
    renv.update(self.make_build_env)
    meson.compile(
        self,
        self.make_dir,
        self.make_build_args,
        renv,
        self.make_wrapper + self.make_build_wrapper,
    )


def do_check(self):
    renv = dict(self.make_env)
    renv.update(self.make_check_env)
    meson.test(
        self,
        self.make_dir,
        self.make_check_args,
        renv,
        self.make_wrapper + self.make_check_wrapper,
    )


def do_install(self):
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
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.build_style_defaults = [
        ("make_dir", "build"),
    ]
