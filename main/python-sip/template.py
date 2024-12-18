pkgname = "python-sip"
pkgver = "6.9.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "custom:sip"
url = "https://github.com/Python-SIP/sip"
source = f"$(PYPI_SITE)/s/sip/sip-{pkgver}.tar.gz"
sha256 = "7904be5190d7879952563b78a3af0e58fa27d9525af7f53f93eac7a83b433e7b"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
