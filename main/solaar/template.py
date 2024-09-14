pkgname = "solaar"
pkgver = "1.1.13"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-dbus",
    "python-evdev",
    "python-gobject",
    "python-psutil",
    "python-pyudev",
    "python-pyyaml",
    "python-xlib",
]
pkgdesc = "Device manager for Logitech devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://pwr-solaar.github.io/Solaar"
source = (
    f"https://github.com/pwr-Solaar/Solaar/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "54cfff1240192e9200400cbe06d2427f1ea41c76f77afafa2dd3fc5d03395adc"
# no tests
options = ["!check"]
