pkgname = "python-psutil"
pkgver = "6.1.0"
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
sha256 = "353815f59a7f64cdaca1c0307ee13558a0512f6db064e92fe833784f08539c7a"
# cwd import memes
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
