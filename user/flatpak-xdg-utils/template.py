pkgname = "flatpak-xdg-utils"
pkgver = "1.0.6"
pkgrel = 0
build_style = "meson"
configure_args = ["--bindir=/usr/lib/flatpak-xdg-utils"]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["glib-devel"]
checkdepends = ["dbus"]
pkgdesc = "Launch programs outside of containers"
license = "LGPL-2.1-or-later"
url = "https://github.com/flatpak/flatpak-xdg-utils"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a48e3e4b5591f2c13e867ac095035c0b5ba8c89e1a38058d46312ae7df972b84"
# FIXME cfi, sigill on tests
hardening = ["vis", "!cfi"]
