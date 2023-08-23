pkgname = "python-twisted"
pkgver = "22.10.0"
pkgrel = 1
build_style = "python_module"
make_check_target = "tests"
hostmakedepends = ["python-setuptools", "python-incremental"]
makedepends = ["python-devel"]
depends = [
    "python-attrs",
    "python-automat",
    "python-cryptography",
    "python-constantly",
    "python-h2",
    "python-hyperlink",
    "python-idna",
    "python-incremental",
    "python-service-identity",
    "python-priority",
    "python-pyserial",
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
source = f"$(PYPI_SITE)/T/Twisted/Twisted-{pkgver}.tar.gz"
sha256 = "32acbd40a94f5f46e7b42c109bfae2b302250945561783a8b7a059048f2d4d31"
# unpackaged checkdepends etc.
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
