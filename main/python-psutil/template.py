pkgname = "python-psutil"
pkgver = "6.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
]
makedepends = ["linux-headers"]
checkdepends = ["python-pytest-xdist"]
depends = ["python"]
pkgdesc = "Process and system monitoring module for Python"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "BSD-3-Clause"
url = "https://github.com/giampaolo/psutil"
source = f"$(PYPI_SITE)/p/psutil/psutil-{pkgver}.tar.gz"
sha256 = "cf8496728c18f2d0b45198f06895be52f36611711746b7f30c464b422b50e2f5"
# cwd import memes
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
