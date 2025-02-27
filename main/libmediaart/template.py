pkgname = "libmediaart"
pkgver = "1.9.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dimage_library=gdk-pixbuf"]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["gdk-pixbuf-devel", "glib-devel"]
pkgdesc = "Library for handling media art caches"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libmediaart"
source = f"$(GNOME_SITE)/libmediaart/{pkgver[:-2]}/libmediaart-{pkgver}.tar.xz"
sha256 = "c3bc5025d7db380587f9c8eb800c611f6b5a16d6b4b78fcff93f62876a677f17"
options = ["!cross"]


@subpackage("libmediaart-devel")
def _(self):
    return self.default_devel()
