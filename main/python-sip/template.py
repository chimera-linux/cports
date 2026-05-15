pkgname = "python-sip"
pkgver = "6.15.3"
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
sha256 = "bb2516983f9f716d321e5157c00d0de0c12422eba73b8f43a44610a0f6622438"
# pypi tarball does not contain tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
