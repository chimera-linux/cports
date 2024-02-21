pkgname = "solaar"
pkgver = "1.1.11"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-evdev",
    "python-pyudev",
    "python-psutil",
    "python-pyyaml",
    "python-xlib",
    "python-gobject",
    "python-dbus",
]
pkgdesc = "Device manager for Logitech devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://pwr-solaar.github.io/Solaar"
source = (
    f"https://github.com/pwr-Solaar/Solaar/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "2b292da8923e19a4a7a459d6fcd1119ce157cb579fd00077f87633c0dedfbba5"
# no tests
options = ["!check"]
