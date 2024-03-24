pkgname = "gsettings-desktop-schemas"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gobject-introspection"]
makedepends = ["glib-devel"]
depends = [
    "fonts-cantarell-otf",
    "fonts-source-code-pro-otf",
    "adwaita-icon-theme",
    "chimera-artwork",
]
pkgdesc = "Collection of GSettings schemas"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "493a46a1161b6388d57aa72f632a79ce96c42d5ffbd1d0b00f496ec5876f8575"
options = ["!cross"]


@subpackage("gsettings-desktop-schemas-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
