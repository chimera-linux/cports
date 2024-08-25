pkgname = "cinnamon-menus"
pkgver = "6.2.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddeprecated_warnings=false",
    "-Denable_debug=false",
    "-Denable_docs=true",
]
hostmakedepends = ["gobject-introspection", "gtk-doc-tools", "meson", "pkgconf"]
makedepends = ["glib-devel"]
pkgdesc = "Cinnamon menu library"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-menus/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "95170602c5291db6f5031dfc245ebf61872ff93860fb1fc18ec433bec638cf16"
options = ["!cross"]


@subpackage("cinnamon-menus-devel")
def _(self):
    return self.default_devel()
