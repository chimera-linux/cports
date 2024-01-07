pkgname = "python-twisted"
pkgver = "23.10.0"
pkgrel = 1
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
sha256 = "987847a0790a2c597197613686e2784fd54167df3a55d0fb17c8412305d76ce5"
# unpackaged checkdepends etc.
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
