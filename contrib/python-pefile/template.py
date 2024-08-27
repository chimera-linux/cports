pkgname = "python-pefile"
pkgver = "2024.8.26"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python library for PE files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/erocarrera/pefile"
source = f"$(PYPI_SITE)/p/pefilE/pefile-{pkgver}.tar.gz"
sha256 = "3ff6c5d8b43e8c37bb6e6dd5085658d658a7a0bdcd20b6a07b1fcfc1c4e9d632"
# tests not included
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
