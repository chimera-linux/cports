pkgname = "libmediaart"
pkgver = "1.9.7"
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
sha256 = "2b43dd9f54f0d8d0b89e2addb83341ab06d7b98cb1b2e704383584af9c560f6b"
options = ["!cross"]


@subpackage("libmediaart-devel")
def _(self):
    return self.default_devel()
