pkgname = "python-xlib"
pkgver = "0.33"
pkgrel = 3
build_style = "python_pep517"
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-six"]
checkdepends = [
    "python-mock",
    "python-pytest-xdist",
    "python-six",
    "xserver-xorg-xvfb",
]
pkgdesc = "Xlib in pure Python"
license = "LGPL-2.1-or-later"
url = "https://github.com/python-xlib/python-xlib"
source = f"{url}/releases/download/{pkgver}/python-xlib-{pkgver}.tar.bz2"
sha256 = "b7a45aaf919915f4908e4b2d79fc2ff3abbbec3b801a45162b3d0f67ed581b37"
