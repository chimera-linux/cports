pkgname = "python-scikit_build_core"
pkgver = "0.11.1"
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
sha256 = "4e5988df5cd33f0bdb9967b72663ca99f50383c9bc21d8b24fa40c0661ae72b7"
# needs virtualenv
options = ["!check"]
