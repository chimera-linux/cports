pkgname = "python-scikit_build_core"
pkgver = "0.10.7"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://scikit-build-core.readthedocs.io"
source = f"$(PYPI_SITE)/s/scikit_build_core/scikit_build_core-{pkgver}.tar.gz"
sha256 = "04cbb59fe795202a7eeede1849112ee9dcbf3469feebd9b8b36aa541336ac4f8"
# needs virtualenv
options = ["!check"]
