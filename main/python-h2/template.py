pkgname = "python-h2"
pkgver = "4.1.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-hpack", "python-hyperframe"]
checkdepends = ["python-pytest", "python-hypothesis"] + list(depends)
pkgdesc = "Python implementation of HTTP/2 state machine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-hyper/h2"
source = f"$(PYPI_SITE)/h/h2/h2-{pkgver}.tar.gz"
sha256 = "a83aca08fbe7aacb79fec788c9c0bac936343560ed9ec18b82a13a12c28d2abb"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
