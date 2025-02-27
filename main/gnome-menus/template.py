pkgname = "gnome-menus"
pkgver = "3.36.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "libtool",
    "pkgconf",
]
makedepends = ["glib-devel"]
pkgdesc = "GNOME menu definitions"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-menus"
source = f"$(GNOME_SITE)/gnome-menus/{pkgver[:-2]}/gnome-menus-{pkgver}.tar.xz"
sha256 = "d9348f38bde956fc32753b28c1cde19c175bfdbf1f4d5b06003b3aa09153bb1f"


@subpackage("gnome-menus-devel")
def _(self):
    return self.default_devel()
