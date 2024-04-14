pkgname = "python-zope.interface"
pkgver = "6.3"
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
sha256 = "f83d6b4b22262d9a826c3bd4b2fbfafe1d0000f085ef8e44cd1328eea274ae6a"
# not functional yet
options = ["!check"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob("python3*"):
        self.install_file(
            "src/zope/__init__.py",
            str((f / "site-packages/zope").relative_to(self.destdir)),
        )
    self.install_license("LICENSE.txt")
