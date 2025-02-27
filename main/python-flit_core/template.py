pkgname = "python-flit_core"
pkgver = "3.11.0"
pkgrel = 0
hostmakedepends = ["python"]
checkdepends = ["python-pytest", "python-testpath"]
depends = ["python"]
pkgdesc = "Simplified PEP 517 packaging backend"
license = "BSD-3-Clause"
url = "https://flit.pypa.io"
source = f"$(PYPI_SITE)/f/flit_core/flit_core-{pkgver}.tar.gz"
sha256 = "6ceeee3219e9d2ea282041f3e027c441597b450b33007cb81168e887b6113a8f"
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
