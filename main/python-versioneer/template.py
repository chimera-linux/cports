pkgname = "python-versioneer"
pkgver = "0.29"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Version-string manager for python-setuptools projects"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/python-versioneer/python-versioneer"
source = f"$(PYPI_SITE)/v/versioneer/versioneer-{pkgver}.tar.gz"
sha256 = "5ab283b9857211d61b53318b7c792cf68e798e765ee17c27ade9f6c924235731"


def check(self):
    self.do("python", "setup.py", "make_versioneer")
    self.do("python", "-m", "unittest", "discover", "test")
