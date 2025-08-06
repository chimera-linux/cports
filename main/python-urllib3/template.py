pkgname = "python-urllib3"
pkgver = "2.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
pkgdesc = "HTTP library with thread-safe connection pooling"
license = "MIT"
url = "https://urllib3.readthedocs.io"
source = f"$(PYPI_SITE)/u/urllib3/urllib3-{pkgver}.tar.gz"
sha256 = "3fc47733c7e419d4bc3f6b3dc2b4f890bb743906a30d56ba4a5bfa4bbff92760"
# unpackaged dependency
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
