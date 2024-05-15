pkgname = "libpanel"
pkgver = "1.6.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libpanel"
source = f"$(GNOME_SITE)/libpanel/{'.'.join(pkgver.rsplit('.')[:-1])}/libpanel-{pkgver}.tar.xz"
sha256 = "b773494a3c69300345cd8e27027448d1189183026cc137802f886417c6ea30b6"
# gobject-introspection
options = ["!cross"]


@subpackage("libpanel-devel")
def _devel(self):
    return self.default_devel()
