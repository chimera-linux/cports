pkgname = "python-pytz"
pkgver = "2025.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
depends = ["python", "tzdb"]
pkgdesc = "Python timezone library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pythonhosted.org/pytz"
source = f"$(PYPI_SITE)/p/pytz/pytz-{pkgver}.tar.gz"
sha256 = "c2db42be2a2518b28e65f9207c4d05e6ff547d1efa4086469ef855e4ab70178e"
broken_symlinks = ["usr/lib/python*/site-packages/pytz/zoneinfo"]
# TODO
options = ["!check"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/pytz/zoneinfo"
    ):
        self.rm(f, recursive=True)
        f.symlink_to("/usr/share/zoneinfo")

    self.install_license("LICENSE.txt")
