pkgname = "python-flit_core"
pkgver = "3.10.1"
pkgrel = 0
hostmakedepends = ["python"]
checkdepends = ["python-pytest", "python-testpath"]
depends = ["python"]
pkgdesc = "Simplified PEP 517 packaging backend"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://flit.pypa.io"
source = f"$(PYPI_SITE)/f/flit_core/flit_core-{pkgver}.tar.gz"
sha256 = "66e5b87874a0d6e39691f0e22f09306736b633548670ad3c09ec9db03c5662f7"
# missing checkdepends
options = ["!check"]


def build(self):
    self.do("python", "-m", "flit_core.wheel")


def check(self):
    self.do("python", "-m", "pytest", "flit_core/tests")


def install(self):
    from cbuild.util import python

    self.do(
        "python",
        "bootstrap_install.py",
        "--install-root",
        self.chroot_destdir,
        f"dist/flit_core-{pkgver}-py3-none-any.whl",
    )
    python.precompile(self, "usr/lib")
    self.install_license("LICENSE")
