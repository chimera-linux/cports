pkgname = "python-psutil"
pkgver = "7.0.0"
pkgrel = 1
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
license = "BSD-3-Clause"
url = "https://github.com/giampaolo/psutil"
source = f"$(PYPI_SITE)/p/psutil/psutil-{pkgver}.tar.gz"
sha256 = "7be9c3eba38beccb6495ea33afd982a44074b78f28c434a1f51cc07fd315c456"
# cwd import memes
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
