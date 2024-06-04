pkgname = "python-more-itertools"
pkgver = "10.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = ["python-pytest"]
pkgdesc = "More routines for operating on iterables, beyond itertools"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/more-itertools/more-itertools"
source = f"$(PYPI_SITE)/m/more-itertools/more-itertools-{pkgver}.tar.gz"
sha256 = "e5d93ef411224fbcef366a6e8ddc4c5781bc6359d43412a65dd5964e46111463"


def post_install(self):
    self.install_license("LICENSE")
