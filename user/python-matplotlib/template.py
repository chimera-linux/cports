pkgname = "python-matplotlib"
pkgver = "3.10.7"
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
sha256 = "0678f04e55c839c543a3803a7a13ab427f488ff396d85ffbad7d427f6fdcbbc3"
# check: ImportError: cannot import name '_c_internal_utils' from 'matplotlib'
options = ["!check"]
