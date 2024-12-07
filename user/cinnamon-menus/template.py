pkgname = "cinnamon-menus"
pkgver = "6.4.0"
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
sha256 = "9cad5ac61900492f66c91810fd13bed9dc37b49ec0b9bbc0bbe9ebf48ee45452"
options = ["!cross"]


@subpackage("cinnamon-menus-devel")
def _(self):
    return self.default_devel()
