pkgname = "python-psutil"
pkgver = "5.9.5"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "python-devel"]
makedepends = ["linux-headers"]
depends = ["python"]
pkgdesc = "Process and system monitoring module for Python"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "BSD-3-Clause"
url = "https://github.com/giampaolo/psutil"
source = f"$(PYPI_SITE)/p/psutil/psutil-{pkgver}.tar.gz"
sha256 = "5410638e4df39c54d957fc51ce03048acd8e6d60abc0f5107af51e5fb566eb3c"
# testing requires a lot of additional modules
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
