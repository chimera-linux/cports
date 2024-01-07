pkgname = "libmanette"
pkgver = "0.2.6"
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
url = "https://gitlab.gnome.org/aplazas/libmanette"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "63653259a821ec7d90d681e52e757e2219d462828c9d74b056a5f53267636bac"


@subpackage("libmanette-devel")
def _devel(self):
    return self.default_devel()
