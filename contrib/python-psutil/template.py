pkgname = "python-psutil"
pkgver = "5.9.8"
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
sha256 = "6be126e3225486dff286a8fb9a06246a5253f4c7c53b475ea5f5ac934e64194c"
# testing requires a lot of additional modules
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
