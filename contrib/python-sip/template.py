pkgname = "python-sip"
pkgver = "6.8.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-packaging",
    "python-setuptools",
]
pkgdesc = "Tool for making python bindings for C/C++ libraries"
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:sip"
url = "https://www.riverbankcomputing.com/software/sip"
source = f"$(PYPI_SITE)/s/sip/sip-{pkgver}.tar.gz"
sha256 = "888547b018bb24c36aded519e93d3e513d4c6aa0ba55b7cc1affbd45cf10762c"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
