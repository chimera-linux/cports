pkgname = "python-more-itertools"
pkgver = "10.6.0"
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
sha256 = "2cd7fad1009c31cc9fb6a035108509e6547547a7a738374f10bd49a09eb3ee3b"


def post_install(self):
    self.install_license("LICENSE")
