pkgname = "solaar"
pkgver = "1.1.12"
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
sha256 = "2abe9b994aa8306adc9955544bc5e953c98e20da9df03f559e9d2d3d8e2f1c8c"
# no tests
options = ["!check"]
