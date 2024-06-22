pkgname = "python-sip"
pkgver = "6.8.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-packaging"]
pkgdesc = "Tool for making python bindings for C/C++ libraries"
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:sip"
url = "https://github.com/Python-SIP/sip"
source = f"$(PYPI_SITE)/s/sip/sip-{pkgver}.tar.gz"
sha256 = "c8f4032f656de3fedbf81243cdbc9e9fd4064945b8c6961eaa81f03cd88554cb"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
