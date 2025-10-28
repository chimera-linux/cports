pkgname = "bubblejail"
pkgver = "0.10.0"
pkgrel = 0
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
    "python-cattrs",
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
sha256 = "f63800d38b2e63066546586476781563afe153ae9f570f817d78c49e797e5b2f"
