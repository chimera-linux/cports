pkgname = "python-priority"
pkgver = "2.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest", "python-hypothesis"]
pkgdesc = "Python implementation of HTTP/2 priority"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-hyper/priority"
source = f"$(PYPI_SITE)/p/priority/priority-{pkgver}.tar.gz"
sha256 = "c965d54f1b8d0d0b19479db3924c7c36cf672dbf2aec92d43fbdaf4492ba18c0"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
