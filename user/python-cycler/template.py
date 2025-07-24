pkgname = "python-cycler"
pkgver = "0.12.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python library for composable cycles"
license = "BSD-3-Clause"
url = "https://matplotlib.org/cycler"
source = (
    f"https://github.com/matplotlib/cycler/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "e83c1956b154ceb252c32e079ac7a95860a76c9ce894858dd082cc881008cae0"


def post_install(self):
    self.install_license("LICENSE")
