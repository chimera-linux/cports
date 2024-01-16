pkgname = "python-jsonschema"
pkgver = "4.21.0"
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
sha256 = "3ba18e27f7491ea4a1b22edce00fb820eec968d397feb3f9cb61d5894bb38167"


def post_install(self):
    self.install_license("COPYING")
