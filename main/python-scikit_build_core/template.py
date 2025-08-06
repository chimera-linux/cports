pkgname = "python-scikit_build_core"
pkgver = "0.11.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["cmake", "python-pathspec", "python-packaging"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python CMake adaptor"
license = "Apache-2.0"
url = "https://scikit-build-core.readthedocs.io"
source = f"$(PYPI_SITE)/s/scikit_build_core/scikit_build_core-{pkgver}.tar.gz"
sha256 = "8f0a1edb86cb087876f3c699d2a2682012efd8867b390ed37355f13949d0628e"
# needs virtualenv
options = ["!check"]
