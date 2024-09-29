pkgname = "gsettings-desktop-schemas"
pkgver = "47.1"
pkgrel = 1
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
source = f"$(GNOME_SITE)/gsettings-desktop-schemas/{pkgver[:-2]}/gsettings-desktop-schemas-{pkgver}.tar.xz"
sha256 = "a60204d9c9c0a1b264d6d0d134a38340ba5fc6076a34b84da945d8bfcc7a2815"
options = ["!cross"]


@subpackage("gsettings-desktop-schemas-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
