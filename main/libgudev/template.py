pkgname = "libgudev"
pkgver = "238"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled", "-Dvapi=enabled"]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["glib-devel", "udev-devel", "vala-devel"]
pkgdesc = "GObject bindings for libudev"
license = "LGPL-2.1-or-later"
url = "http://wiki.gnome.org/Projects/libgudev"
source = f"$(GNOME_SITE)/libgudev/{pkgver}/libgudev-{pkgver}.tar.xz"
sha256 = "61266ab1afc9d73dbc60a8b2af73e99d2fdff47d99544d085760e4fa667b5dd1"


@subpackage("libgudev-devel")
def _(self):
    return self.default_devel()
