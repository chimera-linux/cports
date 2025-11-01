pkgname = "python-asgiref"
pkgver = "3.10.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest", "python-pytest-asyncio"]
pkgdesc = "ASGI specs, helper code, and adapters"
license = "BSD-3-Clause"
url = "https://github.com/django/asgiref"
source = f"$(PYPI_SITE)/a/asgiref/asgiref-{pkgver}.tar.gz"
sha256 = "d89f2d8cd8b56dada7d52fa7dc8075baa08fb836560710d38c292a7a3f78c04e"


def post_install(self):
    self.install_license("LICENSE")
