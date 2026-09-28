pkgname = "python-setuptools_scm"
pkgver = "10.0.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-packaging",
    "python-setuptools",
    "python-vcs_versioning",
    "python-wheel",
]
depends = [
    "python",
    "python-packaging",
    "python-setuptools",
    "python-typing_extensions",
    "python-vcs_versioning",
]
pkgdesc = "Manage Python package versions with SCM tags"
license = "MIT"
url = "https://github.com/pypa/setuptools_scm"
source = f"$(PYPI_SITE)/s/setuptools-scm/setuptools_scm-{pkgver}.tar.gz"
sha256 = "bbba8fe754516cdefd017f4456721775e6ef9662bd7887fb52ae26813d4838c3"
# tests fail when the package is not installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
