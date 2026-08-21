pkgname = "xdg-dbus-proxy"
pkgver = "0.1.8"
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
sha256 = "b6630bd24f8161b0e2546d2acbb014a3b3249f5c0d75f2a863ade898b9034d3d"
