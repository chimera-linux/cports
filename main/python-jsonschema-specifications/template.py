pkgname = "python-jsonschema-specifications"
pkgver = "2025.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-pytest",
    "python-referencing",
]
depends = ["python-referencing"]
pkgdesc = "Json Schema meta-schemas and vocabularies, exposed as a Registry"
license = "MIT"
url = "https://github.com/python-jsonschema/jsonschema-specifications"
source = f"$(PYPI_SITE)/j/jsonschema_specifications/jsonschema_specifications-{pkgver}.tar.gz"
sha256 = "630159c9f4dbea161a6a2205c3011cc4f18ff381b189fff48bb39b9bf26ae608"


def post_install(self):
    self.install_license("COPYING")
