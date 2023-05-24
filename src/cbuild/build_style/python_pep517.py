from cbuild.core import chroot


def do_build(self):
    (self.cwd / self.make_dir).mkdir(parents=True, exist_ok=True)

    benv = dict(self.make_build_env)
    benv["TMPDIR"] = self.make_dir

    self.do(
        "python3",
        "-m",
        "pip",
        "wheel",
        "--no-deps",
        "--use-pep517",
        "--no-clean",
        "--no-build-isolation",
        *self.make_build_args,
        self.make_build_target,
        env=benv,
    )


def do_check(self):
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
        == 0
    ):
        self.do(
            "python3",
            "-m",
            "pytest",
            *self.make_check_args,
            self.make_check_target,
            env=self.make_check_env,
        )
    else:
        self.error("pytest not found")


def do_install(self):
    (self.cwd / self.make_dir).mkdir(parents=True, exist_ok=True)

    benv = dict(self.make_install_env)
    benv["TMPDIR"] = self.make_dir

    itgt = self.make_install_target
    whl = list(map(lambda p: p.name, self.cwd.glob(self.make_install_target)))

    self.do(
        "python3",
        "-m",
        "pip",
        "install",
        "--no-deps",
        "--use-pep517",
        "--no-clean",
        "--no-build-isolation",
        "--prefix",
        "/usr",
        "--root",
        str(self.chroot_destdir),
        *self.make_install_args,
        *whl,
        env=benv,
    )


def use(tmpl):
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    pn = tmpl.pkgname.removeprefix("python-")

    tmpl.build_style_defaults = [
        ("make_build_target", "."),
        ("make_install_target", f"{pn}-{tmpl.pkgver}-*-*-*.whl"),
    ]
