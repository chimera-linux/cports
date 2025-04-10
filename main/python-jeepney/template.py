pkgname = "python-jeepney"
pkgver = "0.9.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Python DBus protocol wrapper"
license = "MIT"
url = "https://gitlab.com/takluyver/jeepney"
source = f"$(PYPI_SITE)/j/jeepney/jeepney-{pkgver}.tar.gz"
sha256 = "cf0e9e845622b81e4a28df94c40345400256ec608d0e55bb8a3feaa9163f5732"
# bunch more deps
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall("usr/lib/python*/site-packages/jeepney/tests", glob=True)
    self.uninstall("usr/lib/python*/site-packages/jeepney/io/tests", glob=True)
