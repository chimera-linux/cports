pkgname = "libwnck"
pkgver = "43.2"
pkgrel = 0
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
sha256 = "55a7444ec1fbb95c086d40967388f231b5c0bbc8cffaa086bf9290ae449e51d5"
options = ["!cross"]


@subpackage("libwnck-devel")
def _(self):
    return self.default_devel()
