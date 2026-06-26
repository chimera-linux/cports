pkgname = "xdg-dbus-proxy"
pkgver = "0.1.7"
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
sha256 = "3ad3d27ba574e178acb5e4d438ba36ace25e3564f899c36f31c56f82c7adbbe7"
