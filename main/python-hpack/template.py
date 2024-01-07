pkgname = "python-hpack"
pkgver = "4.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Python implementation of HTTP/2 header encoding"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-hyper/hpack"
source = f"$(PYPI_SITE)/h/hpack/hpack-{pkgver}.tar.gz"
sha256 = "fc41de0c63e687ebffde81187a948221294896f6bdc0ae2312708df339430095"
# python-hypothesis needed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
