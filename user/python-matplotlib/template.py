pkgname = "python-matplotlib"
pkgver = "3.10.6"
pkgrel = 0
build_style = "python_pep517"
make_build_args = [
    "-Csetup-args=-Dsystem-freetype=true",
    "-Csetup-args=-Dsystem-qhull=true",
]
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-installer",
    "python-meson",
    "python-setuptools_scm",
]
makedepends = [
    "freetype-devel",
    "python-devel",
    "python-pybind11-devel",
    "qhull-devel",
]
depends = [
    "python-contourpy",
    "python-cycler",
    "python-dateutil",
    "python-fonttools",
    "python-kiwisolver",
    "python-numpy",
    "python-packaging",
    "python-pillow",
    "python-pyparsing",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python plotting library"
license = "PSF-2.0"
url = "https://matplotlib.org"
source = f"https://github.com/matplotlib/matplotlib/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b553f599f639a9e19074c7e4f8f4343443483da6cd8819fbfcf6506f155ddf0e"
# check: ImportError: cannot import name '_c_internal_utils' from 'matplotlib'
options = ["!check"]
