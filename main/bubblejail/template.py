pkgname = "bubblejail"
pkgver = "0.9.4"
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
sha256 = "421172ee85ef5b3a72aec0f65e7f80d627291da83c8855f753dfe70ffc4e8b36"
