pkgname = "python-vobject"
pkgver = "0.9.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-dateutil",
    "python-pytz",
    "python-six",
]
checkdepends = [
    "python-pytest",
    *depends,
]
pkgdesc = "Python module for parsing and creating iCalendar and vCard files"
license = "Apache-2.0"
url = "https://github.com/py-vobject/vobject"
# missing test fixtures on pypi
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2adfc34728d9d45b7b9ea215291aab34ae5d1e5a57a566ccd26710757ffd8e0f"


def pre_configure(self):
    with open(self.cwd / "setup.cfg", "w") as outf:
        outf.write(f"[metadata]\nversion = {pkgver}\n")


def check(self):
    self.do("python", "-m", "unittest", "discover", "tests")
