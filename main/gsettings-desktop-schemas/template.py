pkgname = "gsettings-desktop-schemas"
pkgver = "47_rc"
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
    "fonts-cantarell-otf",
    "fonts-source-code-pro-otf",
]
pkgdesc = "Collection of GSettings schemas"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas"
source = f"$(GNOME_SITE)/gsettings-desktop-schemas/{pkgver[:2]}/gsettings-desktop-schemas-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "890d11b57b2464ebbfe6d273a2872659b714fdd1263b10454c6b3ba8099736b8"
options = ["!cross"]


@subpackage("gsettings-desktop-schemas-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
