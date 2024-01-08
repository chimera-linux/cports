pkgname = "python-pytz"
pkgver = "2023.3"
_relver = f"{pkgver}.post1"
pkgrel = 2
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
source = f"$(PYPI_SITE)/p/pytz/pytz-{_relver}.tar.gz"
sha256 = "7b4fddbeb94a1eba4b557da24f19fdf9db575192544270a9101d8509f9f43d7b"
# dependency of pytest
options = ["!check", "brokenlinks"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob(
        "python*/site-packages/pytz/zoneinfo"
    ):
        self.rm(f, recursive=True)
        f.symlink_to("/usr/share/zoneinfo")

    self.install_license("LICENSE.txt")
