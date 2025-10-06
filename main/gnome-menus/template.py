pkgname = "gnome-menus"
pkgver = "3.38.1"
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
sha256 = "1198a91cdbdcfb232df94e71ef5427617d26029e327be3f860c3b0921c448118"


@subpackage("gnome-menus-devel")
def _(self):
    return self.default_devel()
