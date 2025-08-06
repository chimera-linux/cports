pkgname = "python-asgiref"
pkgver = "3.9.1"
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
sha256 = "a5ab6582236218e5ef1648f242fd9f10626cfd4de8dc377db215d5d5098e3142"


def post_install(self):
    self.install_license("LICENSE")
