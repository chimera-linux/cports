pkgname = "python-referencing"
pkgver = "0.35.1"
pkgrel = 0
build_style = "python_pep517"
# the tests in suite/ depend on jsonschema
make_check_args = ["referencing"]
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-attrs",
    "python-iniconfig",
    "python-packaging",
    "python-pluggy",
    "python-pytest",
    "python-pytest-subtests",
    "python-rpds-py",
]
depends = [
    "python-attrs",
    "python-rpds-py",
]
pkgdesc = "Implementation-agnostic implementation of JSON reference resolution"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-jsonschema/referencing"
source = f"$(PYPI_SITE)/r/referencing/referencing-{pkgver}.tar.gz"
sha256 = "25b42124a6c8b632a425174f24087783efb348a6f1e0008e63cd4466fedf703c"


def post_install(self):
    self.install_license("COPYING")
