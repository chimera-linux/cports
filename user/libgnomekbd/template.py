pkgname = "libgnomekbd"
pkgver = "3.28.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = ["gtk+3-devel", "libxklavier-devel"]
pkgdesc = "Gnome keyboard configuration library"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/libgnomekbd"
source = f"$(GNOME_SITE)/libgnomekbd/{pkgver[:-2]}/libgnomekbd-{pkgver}.tar.xz"
sha256 = "22dc59566d73c0065350f5a97340e62ecc7b08c4df19183804bb8be24c8fe870"
options = ["!cross"]


@subpackage("libgnomekbd-devel")
def _(self):
    return self.default_devel()
