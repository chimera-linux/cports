pkgname = "libmanette"
pkgver = "0.2.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala",
]
makedepends = ["glib-devel", "libevdev-devel", "libgudev-devel"]
pkgdesc = "Simple GObject game controller library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libmanette"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "cddd5c02a131072c19c6cde6f2cb2cd57eae7dacb50d14c337efd980baa51a51"


@subpackage("libmanette-devel")
def _devel(self):
    return self.default_devel()
