pkgname = "python-matplotlib"
pkgver = "3.11.1"
pkgrel = 0
build_style = "python_pep517"
make_build_args = [
    "-Csetup-args=-Dsystem-freetype=true",
    "-Csetup-args=-Dsystem-libraqm=true",
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
    "raqm-devel",
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
sha256 = "b8a1eae79e86021624b43484bd07cb318ee83aa5f4ed4c3044dcfdcea63b07fe"
# check: ImportError: cannot import name '_c_internal_utils' from 'matplotlib'
options = ["!check"]

if self.profile().arch == "ppc":
    broken = "error: relocation R_PPC_REL32 cannot be used against symbol '_GLOBAL_OFFSET_TABLE_'; recompile with -fPIC"
