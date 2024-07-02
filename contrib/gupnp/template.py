pkgname = "gupnp"
pkgver = "1.6.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "gssdp-devel",
    "libxml2-devel",
    "linux-headers",
    "libsoup-devel",
    "vala-devel",
]
pkgdesc = "Framework for creating UPnP devices and control points"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GUPnP"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c9dc50e8c78b3792d1b0e6c5c5f52c93e9345d3dae2891e311a993a574f5a04f"


@subpackage("gupnp-devel")
def _devel(self):
    return self.default_devel()
