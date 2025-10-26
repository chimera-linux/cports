pkgname = "python-more-itertools"
pkgver = "10.8.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = ["python-pytest"]
pkgdesc = "More routines for operating on iterables, beyond itertools"
license = "MIT"
url = "https://github.com/more-itertools/more-itertools"
source = f"$(PYPI_SITE)/m/more-itertools/more_itertools-{pkgver}.tar.gz"
sha256 = "f638ddf8a1a0d134181275fb5d58b086ead7c6a72429ad725c67503f13ba30bd"


def post_install(self):
    self.install_license("LICENSE")
