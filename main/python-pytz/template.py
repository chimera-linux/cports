pkgname = "python-pytz"
pkgver = "2022.2.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest"]
depends = ["python", "tzdata"]
pkgdesc = "Python timezone library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pythonhosted.org/pytz"
source = f"$(PYPI_SITE)/p/pytz/pytz-{pkgver}.tar.gz"
sha256 = "cea221417204f2d1a2aa03ddae3e867921971d0d76f14d87abb4414415bbdcf5"
# dependency of pytest
options = ["!check", "brokenlinks"]

def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/pytz/zoneinfo"
    ):
        self.rm(f, recursive = True)
        f.symlink_to("/usr/share/zoneinfo")

    self.install_license("LICENSE.txt")
