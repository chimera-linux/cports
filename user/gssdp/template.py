pkgname = "gssdp"
pkgver = "1.6.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dexamples=false", "-Dmanpages=false"]
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "gtk4-devel",
    "libsoup-devel",
    "linux-headers",
    "vala-devel",
]
pkgdesc = "Resource discovery and announcement over SSDP"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GUPnP"
source = f"$(GNOME_SITE)/gssdp/{pkgver[:-2]}/gssdp-{pkgver}.tar.xz"
sha256 = "2fedb5afdb22cf14d5498a39a773ca89788a250fcf70118783df821e1f3f3446"


@subpackage("gssdp-devel")
def _(self):
    return self.default_devel()
