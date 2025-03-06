pkgname = "python-testpath"
pkgver = "0.6.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python test utilities for working with files and commands"
license = "BSD-3-Clause"
url = "https://testpath.readthedocs.io"
source = f"$(PYPI_SITE)/t/testpath/testpath-{pkgver}.tar.gz"
sha256 = "2f1b97e6442c02681ebe01bd84f531028a7caea1af3825000f52345c30285e0f"


def post_install(self):
    self.install_license("LICENSE")
