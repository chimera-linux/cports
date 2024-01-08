pkgname = "python-jsonschema-specifications"
pkgver = "2023.12.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-referencing",
    "python-pytest",
]
depends = ["python-referencing"]
pkgdesc = "Json Schema meta-schemas and vocabularies, exposed as a Registry"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/python-jsonschema/jsonschema-specifications"
source = f"$(PYPI_SITE)/j/jsonschema_specifications/jsonschema_specifications-{pkgver}.tar.gz"
sha256 = "48a76787b3e70f5ed53f1160d2b81f586e4ca6d1548c5de7085d1682674764cc"


def post_install(self):
    self.install_license("COPYING")
