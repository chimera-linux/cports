pkgname = "python-distutils-extra"
pkgver = "3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["intltool", "python"]
checkdepends = ["intltool", "python-gobject", "python-httplib2"]
pkgdesc = "Enhanced distutils package for Python"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://launchpad.net/python-distutils-extra"
source = f"https://salsa.debian.org/python-team/modules/python-distutils-extra/-/archive/{pkgver}/python-distutils-extra-{pkgver}.tar.bz2"
sha256 = "ee1a6a3f97fd87db6d94007324239da58d9b4860f11f05dd66614565de2e6123"


def check(self):
    self.do("python", "setup.py", "test")
