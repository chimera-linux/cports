pkgname = "libmanette"
pkgver = "0.2.12"
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
sha256 = "48b349267180f1dc34d405a9e1e90ba16f054a19ce907930e679493d911ea1d8"


@subpackage("libmanette-devel")
def _(self):
    return self.default_devel()
