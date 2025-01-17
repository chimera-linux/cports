pkgname = "libgee"
pkgver = "0.20.7"
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
sha256 = "0fdc3cd3d385b3beeb5955ff450752cae76176296ee123be2155d0810d0f89c7"


@subpackage("libgee-devel")
def _(self):
    return self.default_devel()
