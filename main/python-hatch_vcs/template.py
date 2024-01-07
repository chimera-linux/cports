pkgname = "python-hatch_vcs"
pkgver = "0.4.0"
pkgrel = 1
build_style = "python_pep517"
make_check_args = [
    "--deselect",
    "tests/test_build.py::test_basic",
    "--deselect",
    "tests/test_build.py::test_write",
    "--deselect",
    "tests/test_build.py::test_fallback",
    "--deselect",
    "tests/test_build.py::test_root",
    "--deselect",
    "tests/test_build.py::test_metadata",
]
hostmakedepends = ["python-build", "python-installer", "python-hatchling"]
depends = ["python-hatchling", "python-setuptools_scm"]
checkdepends = ["python-pytest", "git"] + depends
pkgdesc = "Hatch plugin for VCS versioning"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/ofek/hatch-vcs"
source = f"$(PYPI_SITE)/h/hatch_vcs/hatch_vcs-{pkgver}.tar.gz"
sha256 = "093810748fe01db0d451fabcf2c1ac2688caefd232d4ede967090b1c1b07d9f7"
# cycle
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
