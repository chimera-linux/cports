pkgname = "python-sip"
pkgver = "6.12.0"
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
sha256 = "083ced94f85315493231119a63970b2ba42b1d38b38e730a70e02a99191a89c6"
# pypi tarball does not contain tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
