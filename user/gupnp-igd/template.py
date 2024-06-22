pkgname = "gupnp-igd"
pkgver = "1.6.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "gssdp-devel",
    "gupnp-devel",
    "libxml2-devel",
]
pkgdesc = "Library to handle UPnP IGD port mapping"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GUPnP"
source = f"$(GNOME_SITE)/gupnp-igd/{pkgver[:-2]}/gupnp-igd-{pkgver}.tar.xz"
sha256 = "4099978339ab22126d4968f2a332b6d094fc44c78797860781f1fc2f11771b74"


@subpackage("gupnp-igd-devel")
def _(self):
    return self.default_devel()
