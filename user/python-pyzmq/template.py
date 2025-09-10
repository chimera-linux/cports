pkgname = "python-pyzmq"
pkgver = "27.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "ninja",
    "pkgconf",
    "python-build",
    "python-cython",
    "python-installer",
    "python-scikit_build_core",
    "python-setuptools",
]
makedepends = [
    "libzmq-devel",
    "python-devel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python bindings for ZeroMQ"
license = "BSD-3-Clause"
url = "https://pypi.org/project/pyzmq"
source = f"$(PYPI_SITE)/p/pyzmq/pyzmq-{pkgver}.tar.gz"
sha256 = "ac0765e3d44455adb6ddbf4417dcce460fc40a05978c08efdf2948072f6db540"
# couldn't make it work
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
