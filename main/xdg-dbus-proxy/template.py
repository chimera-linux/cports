pkgname = "xdg-dbus-proxy"
pkgver = "0.1.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dman=enabled"]
hostmakedepends = [
    "docbook-xsl-nons",
    "meson",
    "ninja",
    "pkgconf",
    "xsltproc",
]
makedepends = ["glib-devel"]
checkdepends = ["dbus"]
pkgdesc = "Filtering proxy for D-Bus connections"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/flatpak/xdg-dbus-proxy"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "061dcfaf8a0650e5fd9d5432dfe88bda749ea0d079dc136304bfecfbce0661fb"
