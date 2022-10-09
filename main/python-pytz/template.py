pkgname = "python-pytz"
pkgver = "2022.4"
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
sha256 = "48ce799d83b6f8aab2020e369b627446696619e79645419610b9facd909b3174"
# dependency of pytest
options = ["!check", "brokenlinks"]

def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/pytz/zoneinfo"
    ):
        self.rm(f, recursive = True)
        f.symlink_to("/usr/share/zoneinfo")

    self.install_license("LICENSE.txt")
