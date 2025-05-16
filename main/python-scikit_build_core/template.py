pkgname = "python-scikit_build_core"
pkgver = "0.11.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-hatch_vcs",
    "python-installer",
]
depends = ["cmake", "python-pathspec", "python-packaging"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python CMake adaptor"
license = "Apache-2.0"
url = "https://scikit-build-core.readthedocs.io"
source = f"$(PYPI_SITE)/s/scikit_build_core/scikit_build_core-{pkgver}.tar.gz"
sha256 = "778fc71f0b8dd0736fa40a43f98603dd32e176977b00244b4e866d79d4564a2d"
# needs virtualenv
options = ["!check"]
