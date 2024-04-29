pkgname = "python-distutils-extra"
pkgver = "2.47"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "Enhanced distutils package for Python"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://launchpad.net/python-distutils-extra"
source = f"https://salsa.debian.org/python-team/modules/python-distutils-extra/-/archive/{pkgver}/python-distutils-extra-{pkgver}.tar.bz2"
sha256 = "bc8979d320d5b79016e65b5e598aa100f96ef04aeba0e389d4dfec7c4d9f6c15"
# TODO
options = ["!check"]
