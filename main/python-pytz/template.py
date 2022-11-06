pkgname = "python-pytz"
pkgver = "2022.6"
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
sha256 = "e89512406b793ca39f5971bc999cc538ce125c0e51c27941bef4568b460095e2"
# dependency of pytest
options = ["!check", "brokenlinks"]

def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/pytz/zoneinfo"
    ):
        self.rm(f, recursive = True)
        f.symlink_to("/usr/share/zoneinfo")

    self.install_license("LICENSE.txt")
