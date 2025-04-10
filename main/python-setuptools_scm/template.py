pkgname = "python-setuptools_scm"
pkgver = "8.2.1"
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
sha256 = "51cfdd1deefc9b8c08d1a61e940a59c4dec39eb6c285d33fa2f1b4be26c7874d"
# tests fail when the package is not installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
