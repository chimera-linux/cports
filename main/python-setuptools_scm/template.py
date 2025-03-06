pkgname = "python-setuptools_scm"
pkgver = "8.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-packaging",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python",
    "python-packaging",
    "python-setuptools",
    "python-typing_extensions",
]
pkgdesc = "Manage Python package versions with SCM tags"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/s/setuptools-scm/setuptools_scm-{pkgver}.tar.gz"
sha256 = "a18396a1bc0219c974d1a74612b11f9dce0d5bd8b1dc55c65f6ac7fd609e8c28"
# tests fail when the package is not installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
