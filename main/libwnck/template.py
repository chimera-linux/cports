pkgname = "libwnck"
pkgver = "43.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxres-devel",
    "startup-notification-devel",
]
pkgdesc = "Window Navigator Construction Kit"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.0-only"
url = "https://gitlab.gnome.org/GNOME/libwnck"
source = f"$(GNOME_SITE)/libwnck/{pkgver[:-2]}/libwnck-{pkgver}.tar.xz"
sha256 = "905bcdb85847d6b8f8861e56b30cd6dc61eae67ecef4cd994a9f925a26a2c1fe"
options = ["!cross"]


@subpackage("libwnck-devel")
def _devel(self):
    return self.default_devel()
