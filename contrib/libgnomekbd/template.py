pkgname = "libgnomekbd"
pkgver = "3.28.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=false"]
hostmakedepends = ["meson", "gettext-tiny", "pkgconf", "glib-devel", "gobject-introspection"]
makedepends = [
    "gtk+3-devel", "libxklavier-devel"
]
pkgdesc = "Gnome keyboard configuration library"
maintainer = "toukoAMG <toukoamg@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/libgnomekbd"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "22dc59566d73c0065350f5a97340e62ecc7b08c4df19183804bb8be24c8fe870"
# needs graphical environment
options = ["!check"]

@subpackage("libgnomekbd-devel")
def _devel(self):
    return self.default_devel()
