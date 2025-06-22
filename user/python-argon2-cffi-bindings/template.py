pkgname = "python-argon2-cffi-bindings"
pkgver = "21.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools_scm",
]
makedepends = ["python-devel"]
depends = ["python-cffi"]
checkdepends = ["python-pytest"]
pkgdesc = "Low-level Argon2 CFFI bindings for Python"
license = "MIT"
url = "https://github.com/hynek/argon2-cffi-bindings"
source = (
    f"$(PYPI_SITE)/a/argon2-cffi-bindings/argon2-cffi-bindings-{pkgver}.tar.gz"
)
sha256 = "bb89ceffa6c791807d1305ceb77dbfacc5aa499891d2c55661c6459651fc39e3"


def post_install(self):
    self.install_license("LICENSE")
