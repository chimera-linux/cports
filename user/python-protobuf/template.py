pkgname = "python-protobuf"
pkgver = "7.34.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "protobuf-protoc",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "protobuf-devel",
    "python-devel",
]
pkgdesc = "Python bindings for protobuf"
license = "BSD-3-Clause"
url = "https://protobuf.dev"
source = f"$(PYPI_SITE)/p/protobuf/protobuf-{pkgver}.tar.gz"
sha256 = "9ce42245e704cc5027be797c1db1eb93184d44d1cdd71811fb2d9b25ad541280"
# meeeeh
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
