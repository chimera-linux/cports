pkgname = "libgudev"
pkgver = "237"
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
sha256 = "0d06b21170d20c93e4f0534dbb9b0a8b4f1119ffb00b4031aaeb5b9148b686aa"


@subpackage("libgudev-devel")
def _devel(self):
    return self.default_devel()
