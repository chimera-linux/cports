pkgname = "ghex"
pkgver = "46.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/ghex"
source = f"$(GNOME_SITE)/ghex/{pkgver[:-2]}/ghex-{pkgver}.tar.xz"
sha256 = "a1c46f3020cb358b8323025db3a539c97d994a4c46f701f48edc6357f7fbcbd1"
options = ["!cross"]


@subpackage("ghex-libs")
def _(self):
    return self.default_libs()


@subpackage("ghex-devel")
def _(self):
    return self.default_devel()
