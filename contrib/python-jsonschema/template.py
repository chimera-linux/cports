pkgname = "python-jsonschema"
pkgver = "4.22.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-jsonschema/jsonschema"
source = f"$(PYPI_SITE)/j/jsonschema/jsonschema-{pkgver}.tar.gz"
sha256 = "5b22d434a45935119af990552c862e5d6d564e8f6601206b305a61fdf661a2b7"


def post_install(self):
    self.install_license("COPYING")
