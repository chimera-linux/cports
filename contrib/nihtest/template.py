pkgname = "nihtest"
pkgver = "1.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Testing tool for command line utilities"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/nih-at/nihtest"
source = f"{url}/releases/download/v{pkgver}/nihtest-{pkgver}.tar.gz"
sha256 = "940033f9b0b955a1a6ebc4eba6beb15bd69e1aeaf40025ff7e41359ff420664b"
# FIXME: no idea how to run these from tests/ tbh
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("manpages/nihtest-case.man", name="nihtest-case", cat=5)
    self.install_man("manpages/nihtest.conf.man", name="nihtest.conf", cat=5)
    self.install_man("manpages/nihtest.man", name="nihtest", cat=1)
