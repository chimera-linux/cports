from cbuild.core import chroot
from cbuild.util import python


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

    ctgt = []
    if len(self.make_check_target) > 0:
        ctgt = [self.make_check_target]

    pybin = python.setup_wheel_venv(
        self,
        ".cbuild-checkenv",
        args=self.make_install_args,
        wrapper=[*self.make_wrapper, *self.make_install_wrapper],
    )

    self.do(
        *self.make_wrapper,
        *self.make_check_wrapper,
        pybin,
        "-m",
        "pytest",
        *self.make_check_args,
        *ctgt,
        env=renv,
        path=[pybin.parent],
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
