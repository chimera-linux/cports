pkgname = "libwnck"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled"]
hostmakedepends = ["meson", "gdk-pixbuf-devel", "gettext-tiny", "pkgconf", "glib-devel", "gobject-introspection"]
makedepends = [
    "startup-notification-devel", "gtk+3-devel", "libxres-devel"
]
pkgdesc = "Library for layout and rendering of text"
maintainer = "toukoAMG <toukoamg@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libwnck"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "905bcdb85847d6b8f8861e56b30cd6dc61eae67ecef4cd994a9f925a26a2c1fe"
# needs graphical environment
options = ["!check"]

@subpackage("libwnck-devel")
def _devel(self):
    return self.default_devel()
