pkgname = "python-aiodns"
pkgver = "3.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pycares"]
pkgdesc = "Simple DNS resolver for asyncio"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/saghul/aiodns"
source = f"$(PYPI_SITE)/a/aiodns/aiodns-{pkgver}.tar.gz"
sha256 = "1073eac48185f7a4150cad7f96a5192d6911f12b4fb894de80a088508c9b3a99"
# no standard pytest tests, requires an internet connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
