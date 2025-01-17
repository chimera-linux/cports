pkgname = "libgee"
pkgver = "0.20.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "gobject-introspection",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = ["glib-devel"]
pkgdesc = "GObject collection library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Libgee"
source = f"$(GNOME_SITE)/libgee/{pkgver[:-2]}/libgee-{pkgver}.tar.xz"
sha256 = "189815ac143d89867193b0c52b7dc31f3aa108a15f04d6b5dca2b6adfad0b0ee"


@subpackage("libgee-devel")
def _(self):
    return self.default_devel()
