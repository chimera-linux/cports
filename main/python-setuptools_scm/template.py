pkgname = "python-setuptools_scm"
pkgver = "8.0.3"
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
]
pkgdesc = "Manage Python package versions with SCM tags"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/s/setuptools-scm/setuptools-scm-{pkgver}.tar.gz"
sha256 = "0169fd70197efda2f8c4d0b2a7a3d614431b488116f37b79d031e9e7ec884d8c"
# tests fail when the package is not installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
