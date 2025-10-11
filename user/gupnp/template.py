pkgname = "gupnp"
pkgver = "1.6.9"
pkgrel = 0
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
sha256 = "2edb6ee3613558e62f538735368aee27151b7e09d4e2e2c51606833da801869b"


@subpackage("gupnp-devel")
def _(self):
    return self.default_devel()
