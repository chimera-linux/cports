pkgname = "libpanel"
pkgver = "1.10.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=disabled"]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["libadwaita-devel"]
pkgdesc = "Dock/panel library for GTK 4"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libpanel"
source = f"$(GNOME_SITE)/libpanel/{'.'.join(pkgver.rsplit('.')[:-1])}/libpanel-{pkgver}.tar.xz"
sha256 = "cc12e8e10f1e4977bd12ad3ffaedcd52ac176348b4af6fe5da686b96325bfe01"
# gobject-introspection
options = ["!cross"]


@subpackage("libpanel-devel")
def _(self):
    return self.default_devel()
