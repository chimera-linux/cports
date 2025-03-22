pkgname = "gsettings-desktop-schemas"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
]
makedepends = ["glib-devel"]
depends = [
    "adwaita-icon-theme",
    "chimera-artwork",
    "fonts-adwaita-ttf",
]
pkgdesc = "Collection of GSettings schemas"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas"
source = f"$(GNOME_SITE)/gsettings-desktop-schemas/{pkgver[:-2]}/gsettings-desktop-schemas-{pkgver}.tar.xz"
sha256 = "e68f155813bf18f865a8b2c8e9d473588b6ccadcafbb666ab788857c6c2d1bd3"
options = ["!cross"]


@subpackage("gsettings-desktop-schemas-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
