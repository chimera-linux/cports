pkgname = "gsettings-desktop-schemas"
pkgver = "45.0"
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
sha256 = "365c8d04daf79b38c8b3dc9626349a024f9e4befdd31fede74b42f7a9fbe0ae2"
options = ["!cross"]


@subpackage("gsettings-desktop-schemas-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
