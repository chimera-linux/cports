pkgname = "python-pyhamcrest"
pkgver = "2.1.0"
pkgrel = 1
build_style = "python_pep517"
make_build_env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python framework for writing matcher objects"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://hamcrest.org"
# no tests on pypi
source = (
    f"https://github.com/hamcrest/PyHamcrest/archive/refs/tags/V{pkgver}.tar.gz"
)
sha256 = "3ce821e78ca4dd0a1d5993186b2cb98ef473ef7910c92116294f8c5f26b6b5ad"


def post_install(self):
    self.install_license("LICENSE.txt")
