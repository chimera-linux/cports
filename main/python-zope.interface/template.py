pkgname = "python-zope.interface"
pkgver = "7.1.0"
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
source = f"$(PYPI_SITE)/z/zope.interface/zope_interface-{pkgver}.tar.gz"
sha256 = "3f005869a1a05e368965adb2075f97f8ee9a26c61898a9e52a9764d93774f237"
# not functional yet
options = ["!check"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob("python3*"):
        self.install_file(
            "src/zope/__init__.py",
            str((f / "site-packages/zope").relative_to(self.destdir)),
        )
    self.install_license("LICENSE.txt")
