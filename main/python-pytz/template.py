pkgname = "python-pytz"
pkgver = "2025.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
depends = ["python", "tzdb"]
pkgdesc = "Python timezone library"
license = "MIT"
url = "https://pythonhosted.org/pytz"
source = f"$(PYPI_SITE)/p/pytz/pytz-{pkgver}.tar.gz"
sha256 = "360b9e3dbb49a209c21ad61809c7fb453643e048b38924c765813546746e81c3"
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
