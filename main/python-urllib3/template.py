pkgname = "python-urllib3"
pkgver = "2.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-hatch_vcs",
    "python-hatchling",
]
depends = ["python"]
pkgdesc = "HTTP library with thread-safe connection pooling"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://urllib3.readthedocs.io"
source = f"$(PYPI_SITE)/u/urllib3/urllib3-{pkgver}.tar.gz"
sha256 = "f8c5449b3cf0861679ce7e0503c7b44b5ec981bec0d1d3795a07f1ba96f0204d"
# unpackaged dependency
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
