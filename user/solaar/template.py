pkgname = "solaar"
pkgver = "1.1.14"
pkgrel = 3
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-dbus",
    "python-evdev",
    "python-gobject",
    "python-psutil",
    "python-pyudev",
    "python-pyyaml",
    "python-typing_extensions",
    "python-xlib",
]
pkgdesc = "Device manager for Logitech devices"
license = "GPL-2.0-or-later"
url = "https://pwr-solaar.github.io/Solaar"
source = (
    f"https://github.com/pwr-Solaar/Solaar/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "8d376a4fe001076a41d3d0bb5f7af079742daf48c37930785a0ecec7da8fbd1f"
# no tests
options = ["!check"]
