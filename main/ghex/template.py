pkgname = "ghex"
pkgver = "48.1"
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
sha256 = "4feab8af967e2763f28bc77a4ddcf54a367aa1d85496fef0501986bd803d89f2"
options = ["!cross"]


@subpackage("ghex-libs")
def _(self):
    return self.default_libs()


@subpackage("ghex-devel")
def _(self):
    return self.default_devel()
