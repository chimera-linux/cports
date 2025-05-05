pkgname = "libpanel"
pkgver = "1.10.0"
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
sha256 = "578ce512278ff2bb5eeebb55099392c52537a5abd9bd0629567f102532b38b25"
# gobject-introspection
options = ["!cross"]


@subpackage("libpanel-devel")
def _(self):
    return self.default_devel()
