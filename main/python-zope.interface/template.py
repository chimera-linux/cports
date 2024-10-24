pkgname = "python-zope.interface"
pkgver = "7.1.1"
pkgrel = 0
build_style = "python_pep517"
# useless setuptools version check
make_build_args = ["--skip-dependency-check"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = ["python-setuptools"]
pkgdesc = "Zope interfaces for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ZPL-2.1"
url = "https://github.com/zopefoundation/zope.interface"
source = f"$(PYPI_SITE)/z/zope.interface/zope.interface-{pkgver}.tar.gz"
sha256 = "4284d664ef0ff7b709836d4de7b13d80873dc5faeffc073abdb280058bfac5e3"
# not functional yet
options = ["!check"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob("python3*"):
        self.install_file(
            "src/zope/__init__.py",
            str((f / "site-packages/zope").relative_to(self.destdir)),
        )
    self.install_license("LICENSE.txt")
