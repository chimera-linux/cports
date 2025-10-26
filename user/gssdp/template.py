pkgname = "gssdp"
pkgver = "1.6.4"
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
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GUPnP"
source = f"$(GNOME_SITE)/gssdp/{pkgver[:-2]}/gssdp-{pkgver}.tar.xz"
sha256 = "ff97fdfb7f561d3e6813b4f6a2145259e7c2eff43cc0e63f3fd031d0b6266032"


@subpackage("gssdp-devel")
def _(self):
    return self.default_devel()
