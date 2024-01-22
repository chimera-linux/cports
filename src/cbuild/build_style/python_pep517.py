from cbuild.core import chroot


def do_build(self):
    (self.cwd / self.make_dir).mkdir(parents=True, exist_ok=True)

    self.do(
        "python3",
        "-m",
        "build",
        "--wheel",
        "--no-isolation",
        *self.make_build_args,
        self.make_build_target,
        env=self.make_build_env,
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
        != 0
    ):
        self.error("pytest not found")

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

    self.do(envpy, "-m", "installer", *self.make_install_args, *whl)
    self.do(
        self.chroot_cwd / ".cbuild-checkenv/bin/python3",
        "-m",
        "pytest",
        *self.make_check_args,
        *ctgt,
        env=self.make_check_env,
        path=[envpy.parent],
    )


def do_install(self):
    (self.cwd / self.make_dir).mkdir(parents=True, exist_ok=True)

    whl = list(
        map(
            lambda p: str(p.relative_to(self.cwd)),
            self.cwd.glob(self.make_install_target),
        )
    )

    self.do(
        "python3",
        "-m",
        "installer",
        "--compile-bytecode",
        "0",
        "--destdir",
        str(self.chroot_destdir),
        *self.make_install_args,
        *whl,
    )


def use(tmpl):
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.build_style_defaults = [
        ("make_build_target", "."),
        ("make_check_target", ""),
        ("make_install_target", "dist/*.whl"),
    ]
