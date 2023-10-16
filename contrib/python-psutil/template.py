pkgname = "python-psutil"
pkgver = "5.9.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["linux-headers"]
depends = ["python"]
pkgdesc = "Process and system monitoring module for Python"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "BSD-3-Clause"
url = "https://github.com/giampaolo/psutil"
source = f"$(PYPI_SITE)/p/psutil/psutil-{pkgver}.tar.gz"
sha256 = "e4b92ddcd7dd4cdd3f900180ea1e104932c7bce234fb88976e2a3b296441225a"
# testing requires a lot of additional modules
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
