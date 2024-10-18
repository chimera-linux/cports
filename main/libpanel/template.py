pkgname = "libpanel"
pkgver = "1.8.1"
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
sha256 = "b87b8fa9b79768cc704243793f0158a040a1e46d37b9889188545a7f7dcaa6fb"
# gobject-introspection
options = ["!cross"]


@subpackage("libpanel-devel")
def _(self):
    return self.default_devel()
