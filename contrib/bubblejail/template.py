pkgname = "bubblejail"
pkgver = "0.9.2"
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
    "python-lxns",
    "python-pyqt6",
    "python-pyxdg",
    "python-tomli-w",
    "xdg-dbus-proxy",
]
checkdepends = [*depends]
pkgdesc = "Bubblewrap based sandboxing for desktop applications"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/igo95862/bubblejail"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3d63bc2d3f4475554582add19f57607b0f57d4f91fbdca6949beae5fbe3190b1"
