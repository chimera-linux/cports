pkgname = "python-sip"
pkgver = "6.11.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = [
    "python-packaging",
    "python-setuptools",
]
pkgdesc = "Tool for making python bindings for C/C++ libraries"
license = "custom:sip"
url = "https://github.com/Python-SIP/sip"
source = f"$(PYPI_SITE)/s/sip/sip-{pkgver}.tar.gz"
sha256 = "3dae4baaf9e9f781d84bf293e0e2938dc7f44b826837889026eba53bd36c81b5"
# pypi tarball does not contain tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
