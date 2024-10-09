from cbuild.core import chroot


def build(self):
    (self.cwd / self.make_dir).mkdir(parents=True, exist_ok=True)

    # we patch main/python-setuptools so these environment variables
    # override whatever the sysconfig module says. this is essential if
    # we're cross building a python extension, since sysconfig will
    # point to the wrong paths in the host system.
    renv = {
        "PYTHON_CROSS_LIBDIR": self.profile().sysroot / "usr/lib",
        "PYTHON_CROSS_INCDIR": self.profile().sysroot
        / f"usr/include/python{self.python_version}",
    }
    renv.update(self.make_env)
    renv.update(self.make_build_env)

    self.do(
        *self.make_wrapper,
        *self.make_build_wrapper,
        "python3",
        "-m",
        "build",
        "--wheel",
        "--no-isolation",
        *self.make_build_args,
        self.make_build_target,
        env=renv,
    )


def check(self):
    renv = dict(self.make_env)
    renv.update(self.make_check_env)

    if (
        chroot.enter(
            "python3",
            "-c",
            "import pytest",
            capture_output=True,
            ro_root=True,
            ro_build=True,
            unshare_all=True,
        ).returncode
        != 0
    ):
        self.error(
            "pytest not found",
            hint="put 'python-pytest' in checkdepends",
        )

    whl = list(
        map(
            lambda p: str(p.relative_to(self.cwd)),
            self.cwd.glob(self.make_install_target),
        )
    )

    ctgt = []
    if len(self.make_check_target) > 0:
        ctgt = [self.make_check_target]

    self.rm(".cbuild-checkenv", recursive=True, force=True)
    self.do(
        "python3",
        "-m",
        "venv",
        "--without-pip",
        "--system-site-packages",
        "--clear",
        ".cbuild-checkenv",
    )

    envpy = self.chroot_cwd / ".cbuild-checkenv/bin/python3"

    self.do(
        *self.make_wrapper,
        *self.make_install_wrapper,
        envpy,
        "-m",
        "installer",
        *self.make_install_args,
        *whl,
    )
    self.do(
        *self.make_wrapper,
        *self.make_check_wrapper,
        self.chroot_cwd / ".cbuild-checkenv/bin/python3",
        # avoid adding cwd to sys.path
        # see https://docs.pytest.org/en/7.1.x/how-to/usage.html#invoke-python
        "/usr/bin/pytest",
        # try to prefer checkenv site-packages when importing
        # https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html
        "--import-mode=append",
        *self.make_check_args,
        *ctgt,
        env=renv,
        path=[envpy.parent],
    )


def install(self):
    renv = dict(self.make_env)
    renv.update(self.make_install_env)

    (self.cwd / self.make_dir).mkdir(parents=True, exist_ok=True)

    whl = list(
        map(
            lambda p: str(p.relative_to(self.cwd)),
            self.cwd.glob(self.make_install_target),
        )
    )

    self.do(
        *self.make_wrapper,
        *self.make_install_wrapper,
        "python3",
        "-m",
        "installer",
        "--compile-bytecode",
        "0",
        "--destdir",
        str(self.chroot_destdir),
        *self.make_install_args,
        *whl,
        env=renv,
    )


def use(tmpl):
    tmpl.build = build
    tmpl.check = check
    tmpl.install = install

    tmpl.build_style_defaults = [
        ("make_build_target", "."),
        ("make_check_target", ""),
        ("make_install_target", "dist/*.whl"),
    ]
