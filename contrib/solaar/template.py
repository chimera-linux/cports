pkgname = "solaar"
pkgver = "1.1.9"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = [
    "python-evdev",
    "python-pyudev",
    "python-psutil",
    "python-pyyaml",
    "python-xlib",
    "python-gobject",
]
checkdepends = list(depends)
pkgdesc = "Device manager for Logitech devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://pwr-solaar.github.io/Solaar"
source = (
    f"https://github.com/pwr-Solaar/Solaar/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "3cb0cb4c79ef2ea0ac7c9adc9c4a6f4f15d28e99ff2df33850de0520ced9f116"
