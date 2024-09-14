pkgname = "python-asgiref"
pkgver = "3.8.1"
pkgrel = 1
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
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "BSD-3-Clause"
url = "https://github.com/django/asgiref"
source = f"$(PYPI_SITE)/a/asgiref/asgiref-{pkgver}.tar.gz"
sha256 = "c343bd80a0bec947a9860adb4c432ffa7db769836c64238fc34bdc3fec84d590"


def post_install(self):
    self.install_license("LICENSE")
