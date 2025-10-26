pkgname = "python-hid"
pkgver = "1.0.8"
pkgrel = 0
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
sha256 = "5ca129a7b9434ace5e3e429c1092a16792feffaf067a46b666e9c586872cdcfe"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
