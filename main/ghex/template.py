pkgname = "ghex"
pkgver = "50.4"
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
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/ghex"
source = f"$(GNOME_SITE)/ghex/{pkgver[:-2]}/ghex-{pkgver}.tar.xz"
sha256 = "e2bcf62438edaf04ca961aef8dafd35a2d208aa45f00ee557000b37214c0972e"
options = ["!cross"]


@subpackage("ghex-libs")
def _(self):
    return self.default_libs()


@subpackage("ghex-devel")
def _(self):
    return self.default_devel()
