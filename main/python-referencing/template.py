pkgname = "python-referencing"
pkgver = "0.36.2"
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
sha256 = "df2e89862cd09deabbdba16944cc3f10feb6b3e6f18e902f7cc25609a34775aa"


def post_install(self):
    self.install_license("COPYING")
