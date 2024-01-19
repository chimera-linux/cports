pkgname = "python-jsonschema"
pkgver = "4.21.1"
pkgrel = 0
build_style = "python_pep517"
# needs pip
make_check_args = ["-k", "not test_license"]
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-pytest",
    "python-jsonschema-specifications",
    "python-referencing",
]
depends = [
    "python-attrs",
    "python-jsonschema-specifications",
    "python-referencing",
    "python-rpds-py",
]
pkgdesc = "Implementation of the JSON Schema specification for Python"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/python-jsonschema/jsonschema"
source = f"$(PYPI_SITE)/j/jsonschema/jsonschema-{pkgver}.tar.gz"
sha256 = "85727c00279f5fa6bedbe6238d2aa6403bedd8b4864ab11207d07df3cc1b2ee5"


def post_install(self):
    self.install_license("COPYING")
