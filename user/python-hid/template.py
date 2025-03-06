pkgname = "python-hid"
pkgver = "1.0.6"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python", "hidapi"]
pkgdesc = "Python bindings for hidapi"
license = "MIT"
url = "https://github.com/apmorton/pyhidapi"
source = f"$(PYPI_SITE)/h/hid/hid-{pkgver}.tar.gz"
sha256 = "48d764d7ae9746ba123b96dbf457893ca80268b7791c4b1d2e051310eeb83860"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
