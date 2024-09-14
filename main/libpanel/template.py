pkgname = "libpanel"
pkgver = "1.8.0"
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
sha256 = "5a9b6b54452fa1903a2fd64ba62278ef94b9b11659b7e1a5fda3518b66cd39c3"
# gobject-introspection
options = ["!cross"]


@subpackage("libpanel-devel")
def _(self):
    return self.default_devel()
