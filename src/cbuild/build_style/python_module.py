# FIXME: cross support

from cbuild.core import chroot


def do_build(self):
    self.do(
        "python3",
        "setup.py",
        "build",
        *self.make_build_args,
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
        == 0
    ):
        ctgt = []
        if len(self.make_check_target) > 0:
            ctgt = [self.make_check_target]

        self.do(
            "python3",
            "-m",
            "pytest",
            *self.make_check_args,
            *ctgt,
            env=self.make_check_env,
        )
    else:
        ctgt = "test"
        if self.make_check_target:
            ctgt = self.make_check_target

        self.do(
            "python3",
            "setup.py",
            ctgt,
            *self.make_check_args,
            env=self.make_check_env,
        )


def do_install(self):
    self.do(
        "python3",
        "setup.py",
        "install",
        "--optimize=1",
        "--prefix=/usr",
        "--root=" + str(self.chroot_destdir),
        *self.make_install_args,
        env=self.make_install_env,
    )


def use(tmpl):
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.build_style_defaults = [
        ("make_check_target", ""),
    ]
