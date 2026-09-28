pkgname = "python-aiodns"
pkgver = "4.0.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-pycares",
    "python-setuptools",
]
depends = ["python-pycares"]
pkgdesc = "Simple DNS resolver for asyncio"
license = "MIT"
url = "https://github.com/saghul/aiodns"
source = f"$(PYPI_SITE)/a/aiodns/aiodns-{pkgver}.tar.gz"
sha256 = "cb10e0c0d2591636716ad2fe402e977c16d71bdaf76bb8cb49e8a6633596f736"
# requires an internet connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
