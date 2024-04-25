pkgname = "python-referencing"
pkgver = "0.35.0"
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
sha256 = "191e936b0c696d0af17ad7430a3dc68e88bc11be6514f4757dc890f04ab05889"


def post_install(self):
    self.install_license("COPYING")
