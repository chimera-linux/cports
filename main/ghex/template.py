pkgname = "ghex"
pkgver = "46.3"
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
sha256 = "ea16595dfba0a97b55dd106305d56ba2baee95de0b13b75e75966cc31f9b3ec9"
options = ["!cross"]


@subpackage("ghex-libs")
def _(self):
    return self.default_libs()


@subpackage("ghex-devel")
def _(self):
    return self.default_devel()
