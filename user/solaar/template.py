pkgname = "solaar"
pkgver = "1.1.19"
pkgrel = 0
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
sha256 = "9392a75bfe9faf14f1e9e5c1a29bfef9d5d8552529c870bdd026915f965230f2"
# no tests
options = ["!check"]
