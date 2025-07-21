pkgname = "gupnp"
pkgver = "1.6.8"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["gobject-introspection", "libxslt-progs", "meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "gssdp-devel",
    "libsoup-devel",
    "libxml2-devel",
    "linux-headers",
    "vala-devel",
]
pkgdesc = "Framework for creating UPnP devices and control points"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GUPnP"
source = f"$(GNOME_SITE)/gupnp/{pkgver[:-2]}/gupnp-{pkgver}.tar.xz"
sha256 = "70a003cebd68577293fb3e6af49ff902203bf8768b2fc5d651ddc1f0fa1e11e9"


@subpackage("gupnp-devel")
def _(self):
    return self.default_devel()
