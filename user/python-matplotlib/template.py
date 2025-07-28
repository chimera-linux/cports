pkgname = "python-matplotlib"
pkgver = "3.10.3"
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
sha256 = "d581d3cec14478a0347631f93d534c2acf11bf554670eedd0a200f56ec979d12"
# check: ImportError: cannot import name '_c_internal_utils' from 'matplotlib'
options = ["!check"]
