from cbuild.util import cmake


def configure(self):
    cmake.configure(
        self,
        self.make_dir,
        self.cmake_dir,
        self.configure_args,
        self.configure_env,
        "Ninja" if self.make_cmd == "ninja" else "Unix Makefiles",
    )


def build(self):
    eargs = []

    if len(self.make_build_target) > 0:
        eargs += ["--target", self.make_build_target]

    renv = dict(self.make_env)
    renv.update(self.make_build_env)

    cmake.build(
        self,
        self.make_dir,
        eargs + self.make_build_args,
        renv,
        self.make_wrapper + self.make_build_wrapper,
    )


def check(self):
    renv = dict(self.make_env)
    renv.update(self.make_check_env)

    if len(self.make_check_target) > 0:
        cmake.build(
            self,
            self.make_dir,
            [
                "--target",
                *self.make_check_target.split(),
                *self.make_check_args,
            ],
            renv,
            self.make_wrapper + self.make_check_wrapper,
        )
        return

    cmake.ctest(
        self,
        self.make_dir,
        self.make_check_args,
        renv,
        self.make_wrapper + self.make_check_wrapper,
    )


def install(self):
    renv = dict(self.make_env)
    renv.update(self.make_install_env)
    cmake.install(
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
        ("make_cmd", "ninja"),
        ("make_dir", "build"),
        ("make_check_target", ""),
    ]
