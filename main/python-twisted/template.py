pkgname = "python-twisted"
pkgver = "25.5.0"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "tests"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-incremental",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = [
    "python-attrs",
    "python-automat",
    "python-constantly",
    "python-cryptography",
    "python-h2",
    "python-hyperlink",
    "python-idna",
    "python-incremental",
    "python-openssl",
    "python-priority",
    "python-pyserial",
    "python-service-identity",
    "python-typing_extensions",
    "python-zope.interface",
]
checkdepends = [
    "git",
    "python-appdirs",
    "python-bcrypt",
    "python-hypothesis",
    "python-pyhamcrest",
    *depends,
]
pkgdesc = "Asynchronous framework for Python"
license = "MIT"
url = "https://twistedmatrix.com"
source = f"$(PYPI_SITE)/t/twisted/twisted-{pkgver}.tar.gz"
sha256 = "1deb272358cb6be1e3e8fc6f9c8b36f78eb0fa7c2233d2dbe11ec6fee04ea316"
# unpackaged checkdepends etc.
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
