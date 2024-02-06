pkgname = "python-pytz"
pkgver = "2024.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python", "tzdata"]
pkgdesc = "Python timezone library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pythonhosted.org/pytz"
source = f"$(PYPI_SITE)/p/pytz/pytz-{pkgver}.tar.gz"
sha256 = "2a29735ea9c18baf14b448846bde5a48030ed267578472d8955cd0e7443a9812"
# dependency of pytest
options = ["!check", "brokenlinks"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/pytz/zoneinfo"
    ):
        self.rm(f, recursive=True)
        f.symlink_to("/usr/share/zoneinfo")

    self.install_license("LICENSE.txt")
