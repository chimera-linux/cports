pkgname = "python-zope.interface"
pkgver = "6.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
makedepends = ["python-devel"]
depends = ["python-setuptools"]
pkgdesc = "Zope interfaces for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ZPL-2.1"
url = "https://github.com/zopefoundation/zope.interface"
source = f"$(PYPI_SITE)/z/zope.interface/zope.interface-{pkgver}.tar.gz"
sha256 = "aab584725afd10c710b8f1e6e208dbee2d0ad009f57d674cb9d1b3964037275d"
# not functional yet
options = ["!check"]

def post_install(self):
    for f in (self.destdir / "usr/lib").glob("python3*"):
        self.install_file(
            "src/zope/__init__.py",
            str((f / "site-packages/zope").relative_to(self.destdir))
        )
    self.install_license("LICENSE.txt")
