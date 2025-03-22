pkgname = "libmanette"
pkgver = "0.2.11"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgudev=enabled"]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "hidapi-devel",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["glib-devel", "libevdev-devel", "libgudev-devel"]
pkgdesc = "Simple GObject game controller library"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libmanette"
source = f"$(GNOME_SITE)/libmanette/{pkgver[:-3]}/libmanette-{pkgver}.tar.xz"
sha256 = "b812b94e08632ba62a30960a8de29217a73a2fff5da2f12acc8a5d4771a49a70"


@subpackage("libmanette-devel")
def _(self):
    return self.default_devel()
