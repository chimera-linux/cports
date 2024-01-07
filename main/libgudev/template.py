pkgname = "libgudev"
pkgver = "238"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled", "-Dvapi=enabled"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala",
]
makedepends = ["glib-devel", "udev-devel", "vala-devel"]
pkgdesc = "GObject bindings for libudev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://wiki.gnome.org/Projects/libgudev"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "61266ab1afc9d73dbc60a8b2af73e99d2fdff47d99544d085760e4fa667b5dd1"


@subpackage("libgudev-devel")
def _devel(self):
    return self.default_devel()
