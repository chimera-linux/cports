pkgname = "python-psutil"
pkgver = "5.9.7"
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
sha256 = "3f02134e82cfb5d089fddf20bb2e03fd5cd52395321d1c8458a9e58500ff417c"
# testing requires a lot of additional modules
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
