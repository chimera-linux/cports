pkgname = "python-aiodns"
pkgver = "3.4.0"
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
sha256 = "24b0ae58410530367f21234d0c848e4de52c1f16fbddc111726a4ab536ec1b2f"
# requires an internet connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
