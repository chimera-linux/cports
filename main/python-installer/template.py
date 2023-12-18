pkgname = "python-installer"
pkgver = "0.7.0"
pkgrel = 1
hostmakedepends = ["python", "python-flit_core"]
checkdepends = ["python-pytest-xdist"]
depends = ["python"]
pkgdesc = "Low-level library for installing from a Python wheel"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://installer.readthedocs.io"
source = f"$(PYPI_SITE)/i/installer/installer-{pkgver}.tar.gz"
sha256 = "a26d3e3116289bb08216e0d0f7d925fcef0b0194eedfa0c944bcaaa106c4b631"
# missing checkdepends
options = ["!check"]


def do_build(self):
    self.do("python", "-m", "flit_core.wheel")


def do_check(self):
    self.do("python", "-m", "pytest", env={"PYTHONPATH": "src"})


def do_install(self):
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
