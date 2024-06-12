pkgname = "python-brotli"
pkgver = "1.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python bindings for the Brotli compression library"
maintainer = "q66 <q66@chimera-linux.com>"
license = "MIT"
url = "https://github.com/google/brotli"
source = f"$(PYPI_SITE)/b/brotli/Brotli-{pkgver}.tar.gz"
sha256 = "81de08ac11bcb85841e440c13611c00b67d3bf82698314928d0b676362546724"


def post_install(self):
    self.install_license("LICENSE")
