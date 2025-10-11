pkgname = "libwnck"
pkgver = "43.3"
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
license = "LGPL-2.0-only"
url = "https://gitlab.gnome.org/GNOME/libwnck"
source = f"$(GNOME_SITE)/libwnck/{pkgver[:-2]}/libwnck-{pkgver}.tar.xz"
sha256 = "6af8ac41a8f067ade1d3caaed254a83423b5f61ad3f7a460fcacbac2e192bdf7"
options = ["!cross"]


@subpackage("libwnck-devel")
def _(self):
    return self.default_devel()
