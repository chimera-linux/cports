pkgname = "python-twisted"
pkgver = "24.3.0"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "tests"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-incremental",
    "python-installer",
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
    "python-bcrypt",
    "python-pyhamcrest",
    "python-appdirs",
    "python-hypothesis",
    "git",
] + depends
pkgdesc = "Asynchronous framework for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://twistedmatrix.com"
source = f"$(PYPI_SITE)/t/twisted/twisted-{pkgver}.tar.gz"
sha256 = "6b38b6ece7296b5e122c9eb17da2eeab3d98a198f50ca9efd00fb03e5b4fd4ae"
# unpackaged checkdepends etc.
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
