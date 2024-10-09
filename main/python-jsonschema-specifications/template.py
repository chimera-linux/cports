pkgname = "python-jsonschema-specifications"
pkgver = "2024.10.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-jsonschema/jsonschema-specifications"
source = f"$(PYPI_SITE)/j/jsonschema_specifications/jsonschema_specifications-{pkgver}.tar.gz"
sha256 = "0f38b83639958ce1152d02a7f062902c41c8fd20d558b0c34344292d417ae272"


def post_install(self):
    self.install_license("COPYING")
