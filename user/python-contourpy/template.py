pkgname = "python-contourpy"
pkgver = "1.3.3"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-meson",
]
makedepends = [
    "python-devel",
    "python-pybind11-devel",
]
depends = [
    "python-numpy",
]
checkdepends = ["python-numpy-tests", "python-pytest", *depends]
pkgdesc = "Python library for calculating contours"
license = "BSD-3-Clause"
url = "https://contourpy.readthedocs.io"
source = (
    f"https://github.com/contourpy/contourpy/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c1e4d622e9d4f3081dbdb438b403e50557be7284a41d9a21316414405848ba62"
# check: too many tests depend on matplotlib, circular dependency
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
