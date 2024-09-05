pkgname = "libpanel"
pkgver = "1.7.1"
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
sha256 = "7b60fd83f0f57e7d80f27c3ab40b369d588f93546ba13de6195321e42d3d1429"
# gobject-introspection
options = ["!cross"]


@subpackage("libpanel-devel")
def _(self):
    return self.default_devel()
