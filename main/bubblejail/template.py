pkgname = "bubblejail"
pkgver = "0.9.5"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-jinja2",
    "python-pyxdg",
    "python-tomli-w",
    "scdoc",
]
depends = [
    "bubblewrap",
    "desktop-file-utils",
    "libnotify",
    "libseccomp",
    "python-lxns",
    "python-pyqt6",
    "python-pyxdg",
    "python-tomli-w",
    "xdg-dbus-proxy",
]
checkdepends = [*depends]
pkgdesc = "Bubblewrap based sandboxing for desktop applications"
license = "GPL-3.0-or-later"
url = "https://github.com/igo95862/bubblejail"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cafaca440bf40e7069978a9f9e2c3c3199d01b3c9fa1af080f23cf072b06d188"
