pkgname = "python-hyperframe"
pkgver = "6.0.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python implementation of HTTP/2 framing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-hyper/hyperframe"
source = f"$(PYPI_SITE)/h/hyperframe/hyperframe-{pkgver}.tar.gz"
sha256 = "ae510046231dc8e9ecb1a6586f63d2347bf4c8905914aa84ba585ae85f28a914"
# fails to find itself?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
