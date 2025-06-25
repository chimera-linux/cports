pkgname = "python-aiodns"
pkgver = "3.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-pycares"]
pkgdesc = "Simple DNS resolver for asyncio"
license = "MIT"
url = "https://github.com/saghul/aiodns"
source = f"$(PYPI_SITE)/a/aiodns/aiodns-{pkgver}.tar.gz"
sha256 = "11264edbab51896ecf546c18eb0dd56dff0428c6aa6d2cd87e643e07300eb310"
# requires an internet connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
