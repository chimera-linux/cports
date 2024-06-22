pkgname = "python-sip"
pkgver = "6.8.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python-packaging",
    "python-setuptools",
]
pkgdesc = "Tool for making python bindings for C/C++ libraries"
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:sip"
url = "https://github.com/Python-SIP/sip"
source = f"$(PYPI_SITE)/s/sip/sip-{pkgver}.tar.gz"
sha256 = "5dddd5966e9875d89ecde9d3e6ac63225f9972e4d25c09e20fa22f1819409c70"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
