# FIXME: cross support, check


def configure(self):
    env = {"PKGCONFIG": self.get_tool("PKG_CONFIG")}
    env.update(self.configure_env)

    self.do(
        "python3",
        self.configure_script,
        "configure",
        "--prefix=/usr",
        "--libdir=/usr/lib",
        *self.configure_args,
        env=env,
    )


def build(self):
    self.do(
        "python3",
        self.configure_script,
        self.make_build_target,
        f"-j{self.make_jobs}",
        *self.make_build_args,
        env=self.make_build_env,
    )


def check(self):
    self.do(
        "python3",
        self.configure_script,
        self.make_check_target,
        f"-j{self.make_jobs}",
        *self.make_check_args,
        env=self.make_check_env,
    )


def install(self):
    self.do(
        "python3",
        self.configure_script,
        self.make_install_target,
        "--destdir=" + str(self.chroot_destdir),
        *self.make_install_args,
        env=self.make_install_env,
    )


def use(tmpl):
    tmpl.configure = configure
    tmpl.build = build
    tmpl.check = check
    tmpl.install = install

    tmpl.build_style_defaults = [
        ("configure_script", "waf"),
        ("make_build_target", "build"),
        ("make_install_target", "install"),
        ("make_check_target", "test"),
    ]
