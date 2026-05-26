pkgname = "python-vcs_versioning"
pkgver = "1.1.1"
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
]
pkgdesc = "Manage versions by VCS metadata"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/v/vcs_versioning/vcs_versioning-{pkgver}.tar.gz"
sha256 = "fabd75a3cab7dd8ac02fe24a3a9ba936bf258667b5a62ed468c9a1da0f5775bc"
# tests fail when the package is not installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
