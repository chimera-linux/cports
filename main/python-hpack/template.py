pkgname = "python-hpack"
pkgver = "4.1.0"
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
license = "MIT"
url = "https://github.com/python-hyper/hpack"
source = f"$(PYPI_SITE)/h/hpack/hpack-{pkgver}.tar.gz"
sha256 = "ec5eca154f7056aa06f196a557655c5b009b382873ac8d1e66e79e87535f1dca"
# python-hypothesis needed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
