pkgname = "python-jsonschema"
pkgver = "4.20.0"
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
sha256 = "4f614fd46d8d61258610998997743ec5492a648b33cf478c1ddc23ed4598a5fa"


def post_install(self):
    self.install_license("COPYING")
