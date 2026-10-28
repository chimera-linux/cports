pkgname = "python-sip"
pkgver = "6.17.2"
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
sha256 = "f9e3e765b662b1a93a57440efd3f99a4001bf1bfe282fc0e24566d8d6122de3c"
# pypi tarball does not contain tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
