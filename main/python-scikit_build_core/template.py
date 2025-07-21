pkgname = "python-scikit_build_core"
pkgver = "0.11.3"
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
sha256 = "74baf7cbc089f8621cc0646d9c5679034d5be1b014c10912dc32a4bcd1092506"
# needs virtualenv
options = ["!check"]
