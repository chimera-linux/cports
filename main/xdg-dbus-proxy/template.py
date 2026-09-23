pkgname = "xdg-dbus-proxy"
pkgver = "0.1.9"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dman=enabled"]
hostmakedepends = [
    "docbook-xsl-nons",
    "libxslt-progs",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = ["glib-devel"]
checkdepends = ["dbus"]
pkgdesc = "Filtering proxy for D-Bus connections"
license = "GPL-3.0-or-later"
url = "https://github.com/flatpak/xdg-dbus-proxy"
source = f"{url}/releases/download/{pkgver}/xdg-dbus-proxy-{pkgver}.tar.xz"
sha256 = "5450dda586ec3bb3ca709d311e845487883faa3b09cf562608d7e84f4311dced"
