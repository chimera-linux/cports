pkgname = "python-xlib"
pkgver = "0.33"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-six"]
checkdepends = [
    "python-six",
    "python-pytest-xdist",
    "python-mock",
    "xserver-xorg-xvfb",
]
pkgdesc = "Xlib in pure Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/python-xlib/python-xlib"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "b7a45aaf919915f4908e4b2d79fc2ff3abbbec3b801a45162b3d0f67ed581b37"
# unpackaged checkdepends
options = ["!check"]
