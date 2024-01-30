pkgname = "python-referencing"
pkgver = "0.33.0"
pkgrel = 0
build_style = "python_pep517"
# the tests in suite/ depend on jsonschema
make_check_args = ["referencing"]
hostmakedepends = [
    "python",
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
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/python-jsonschema/referencing"
source = f"$(PYPI_SITE)/r/referencing/referencing-{pkgver}.tar.gz"
sha256 = "c775fedf74bc0f9189c2a3be1c12fd03e8c23f4d371dce795df44e06c5b412f7"


def post_install(self):
    self.install_license("COPYING")
