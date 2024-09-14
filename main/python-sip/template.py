pkgname = "python-sip"
pkgver = "6.8.6"
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
sha256 = "7fc959e48e6ec5d5af8bd026f69f5e24d08b3cb8abb342176f5ab8030cc07d7a"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
