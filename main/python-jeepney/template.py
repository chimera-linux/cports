pkgname = "python-jeepney"
pkgver = "0.8.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Python DBus protocol wrapper"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.com/takluyver/jeepney"
source = f"$(PYPI_SITE)/j/jeepney/jeepney-{pkgver}.tar.gz"
sha256 = "5efe48d255973902f6badc3ce55e2aa6c5c3b3bc642059ef3a91247bcfcc5806"
# bunch more deps
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.uninstall("usr/lib/python*/site-packages/jeepney/tests", glob=True)
    self.uninstall("usr/lib/python*/site-packages/jeepney/io/tests", glob=True)
