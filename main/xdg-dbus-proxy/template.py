pkgname = "xdg-dbus-proxy"
pkgver = "0.1.6"
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
sha256 = "131bf59fce7c7ee7ecbc5d9106d6750f4f597bfe609966573240f7e4952973a1"
