pkgname = "python-installer"
pkgver = "1.0.0"
pkgrel = 0
hostmakedepends = ["python-flit_core"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Low-level library for installing from a Python wheel"
license = "MIT"
url = "https://installer.pypa.io/en/stable"
source = f"$(PYPI_SITE)/i/installer/installer-{pkgver}.tar.gz"
sha256 = "c6d691331621cf3fec4822f5c6f83cab3705f79b316225dc454127411677c71f"
# cycle
options = ["!check"]


def build(self):
    self.do("python", "-m", "flit_core.wheel")


def check(self):
    self.do("python", "-m", "pytest", env={"PYTHONPATH": "src"})


def install(self):
    from cbuild.util import python

    self.do(
        "python",
        "-m",
        "installer",
        "--destdir",
        self.chroot_destdir,
        f"dist/installer-{pkgver}-py3-none-any.whl",
        env={"PYTHONPATH": "src"},
    )
    python.precompile(self, "usr/lib")
    self.install_license("LICENSE")
