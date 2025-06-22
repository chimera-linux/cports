pkgname = "python-argon2-cffi"
pkgver = "25.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-argon2-cffi-bindings",
    "python-cffi",
]
checkdepends = [
    "python-hypothesis",
    "python-pytest",
    *depends,
]
pkgdesc = "Argon2 password hashing for Python"
license = "MIT"
url = "https://github.com/hynek/argon2-cffi"
source = f"$(PYPI_SITE)/a/argon2_cffi/argon2_cffi-{pkgver}.tar.gz"
sha256 = "694ae5cc8a42f4c4e2bf2ca0e64e51e23a040c6a517a85074683d3959e1346c1"


def post_install(self):
    self.install_license("LICENSE")
