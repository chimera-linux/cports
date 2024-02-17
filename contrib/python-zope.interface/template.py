pkgname = "python-zope.interface"
pkgver = "6.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python-setuptools"]
pkgdesc = "Zope interfaces for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ZPL-2.1"
url = "https://github.com/zopefoundation/zope.interface"
source = f"$(PYPI_SITE)/z/zope.interface/zope.interface-{pkgver}.tar.gz"
sha256 = "3b6c62813c63c543a06394a636978b22dffa8c5410affc9331ce6cdb5bfa8565"
# not functional yet
options = ["!check"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob("python3*"):
        self.install_file(
            "src/zope/__init__.py",
            str((f / "site-packages/zope").relative_to(self.destdir)),
        )
    self.install_license("LICENSE.txt")
