pkgname = "python-urllib3"
pkgver = "2.2.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatchling"]
depends = ["python"]
pkgdesc = "HTTP library with thread-safe connection pooling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://urllib3.readthedocs.io"
source = f"$(PYPI_SITE)/u/urllib3/urllib3-{pkgver}.tar.gz"
sha256 = "dd505485549a7a552833da5e6063639d0d177c04f23bc3864e41e5dc5f612168"
# unpackaged dependency
options = ["!check", "brokenlinks"]


def post_install(self):
    self.install_license("LICENSE.txt")
