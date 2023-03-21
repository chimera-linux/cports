pkgname = "gsettings-desktop-schemas"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection"
]
makedepends = ["glib-devel"]
depends = [
    "fonts-cantarell-otf", "fonts-source-code-pro-otf", "adwaita-icon-theme",
    "chimera-artwork",
]
pkgdesc = "Collection of GSettings schemas"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5d5568282ab38b95759d425401f7476e56f8cbf2629885587439f43bd0b84bbe"
options = ["!cross"]

@subpackage("gsettings-desktop-schemas-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
