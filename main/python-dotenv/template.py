pkgname = "python-dotenv"
pkgver = "1.1.0"
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
sha256 = "41f90bc6f5f177fb41f53e87666db362025010eb28f60a01c9143bfa33a2b2d5"


def post_install(self):
    self.install_license("LICENSE")
