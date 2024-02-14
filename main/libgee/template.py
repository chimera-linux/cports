pkgname = "libgee"
pkgver = "0.20.6"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1bf834f5e10d60cc6124d74ed3c1dd38da646787fbf7872220b8b4068e476d4d"


@subpackage("libgee-devel")
def _devel(self):
    return self.default_devel()
