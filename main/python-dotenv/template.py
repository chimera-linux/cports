pkgname = "python-dotenv"
pkgver = "1.0.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = [
    "python-click",
    "python-pytest",
    "python-sh",
]
depends = ["python"]
pkgdesc = "Python module that reads env vars from a .env file"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://saurabh-kumar.com/python-dotenv"
source = f"$(PYPI_SITE)/p/python-dotenv/python-dotenv-{pkgver}.tar.gz"
sha256 = "e324ee90a023d808f1959c46bcbc04446a10ced277783dc6ee09987c37ec10ca"


def post_install(self):
    self.install_license("LICENSE")
