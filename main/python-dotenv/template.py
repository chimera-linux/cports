pkgname = "python-dotenv"
pkgver = "1.1.1"
pkgrel = 0
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
license = "BSD-3-Clause"
url = "https://saurabh-kumar.com/python-dotenv"
source = f"$(PYPI_SITE)/p/python-dotenv/python_dotenv-{pkgver}.tar.gz"
sha256 = "a8a6399716257f45be6a007360200409fce5cda2661e3dec71d23dc15f6189ab"


def post_install(self):
    self.install_license("LICENSE")
