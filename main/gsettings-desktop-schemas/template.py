pkgname = "gsettings-desktop-schemas"
pkgver = "46.1"
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
source = f"$(GNOME_SITE)/gsettings-desktop-schemas/{pkgver[:-2]}/gsettings-desktop-schemas-{pkgver}.tar.xz"
sha256 = "9b88101437a6958ebe6bbd812e49bbf1d09cc667011e415559d847e870468a61"
options = ["!cross"]


@subpackage("gsettings-desktop-schemas-devel")
def _devel(self):
    self.depends += [self.parent]
    return self.default_devel()
