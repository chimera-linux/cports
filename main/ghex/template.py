pkgname = "ghex"
pkgver = "46.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "appstream-glib",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "linux-headers",
]
pkgdesc = "Hex editor for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/ghex"
source = f"$(GNOME_SITE)/ghex/{pkgver[:-2]}/ghex-{pkgver}.tar.xz"
sha256 = "8a13975474eee27719b29ad763f1b24760a1aede6d7da4b623703070bc26e9fd"
options = ["!cross"]


@subpackage("ghex-libs")
def _(self):
    return self.default_libs()


@subpackage("ghex-devel")
def _(self):
    return self.default_devel()
