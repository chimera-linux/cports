pkgname = "python-sip"
pkgver = "6.17.3"
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
sha256 = "e3b5c2d1429a96f2e1fc25b69d4ceb232bc8b7f2395e864c904cec28905642b5"
# pypi tarball does not contain tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
