pkgname = "python-contourpy"
pkgver = "1.3.2"
pkgrel = 0
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
sha256 = "7eec4ace7c075e291b0640b7012c33c46a8d9480d3613f20194a991c1e5774f5"
# check: too many tests depend on matplotlib, circular dependency
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
