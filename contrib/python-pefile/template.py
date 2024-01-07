pkgname = "python-pefile"
pkgver = "2023.2.7"
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
pkgdesc = "Python library for PE files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/erocarrera/pefile"
source = f"$(PYPI_SITE)/p/pefilE/pefile-{pkgver}.tar.gz"
sha256 = "82e6114004b3d6911c77c3953e3838654b04511b8b66e8583db70c65998017dc"
# tests not included
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
