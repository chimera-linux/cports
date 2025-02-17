pkgname = "python-pysol_cards"
pkgver = "0.18.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for dealing cards like various solitaire games"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/shlomif/pysol_cards"
source = f"$(PYPI_SITE)/p/pysol_cards/pysol_cards-{pkgver}.tar.gz"
sha256 = "103c7c0c319e72e836e099bbb47ff54be729d975e35c11ba74d4ac5e4286b8eb"


def post_install(self):
    self.install_license("LICENSE")
