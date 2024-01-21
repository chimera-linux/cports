pkgname = "python-asgiref"
pkgver = "3.7.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-pytest-asyncio"]
pkgdesc = "ASGI specs, helper code, and adapters"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "BSD-3-Clause"
url = "https://github.com/django/asgiref"
source = f"$(PYPI_SITE)/a/asgiref/asgiref-{pkgver}.tar.gz"
sha256 = "9e0ce3aa93a819ba5b45120216b23878cf6e8525eb3848653452b4192b92afed"


def post_install(self):
    self.install_license("LICENSE")
