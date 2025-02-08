pkgname = "python-protobuf"
pkgver = "5.29.3"
pkgrel = 0
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://protobuf.dev"
source = f"$(PYPI_SITE)/p/protobuf/protobuf-{pkgver}.tar.gz"
sha256 = "5da0f41edaf117bde316404bad1a486cb4ededf8e4a54891296f648e8e076620"
# meeeeh
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
