pkgname = "python-twisted"
pkgver = "24.7.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://twistedmatrix.com"
source = f"$(PYPI_SITE)/t/twisted/twisted-{pkgver}.tar.gz"
sha256 = "5a60147f044187a127ec7da96d170d49bcce50c6fd36f594e60f4587eff4d394"
# unpackaged checkdepends etc.
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
