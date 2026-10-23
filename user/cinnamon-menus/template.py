pkgname = "cinnamon-menus"
pkgver = "6.6.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Denable_docs=true"]
hostmakedepends = ["gobject-introspection", "gtk-doc-tools", "meson", "pkgconf"]
makedepends = ["glib-devel"]
pkgdesc = "Cinnamon menu library"
license = "LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-menus/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "87596380720077991f58afdbbabe72d9afd10f56d64043076cf7b09bc6b0f3c1"
options = ["!cross"]


@subpackage("cinnamon-menus-devel")
def _(self):
    return self.default_devel()
