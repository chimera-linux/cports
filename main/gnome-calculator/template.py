pkgname = "gnome-calculator"
pkgver = "46.1"
pkgrel = 2
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "vala",
    "itstool",
    "gobject-introspection",
    "gtk-update-icon-cache",
    "desktop-file-utils",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "gtksourceview-devel",
    "libgee-devel",
    "mpc-devel",
    "libsoup-devel",
    "gsettings-desktop-schemas-devel",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "GNOME calculator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calculator"
source = f"$(GNOME_SITE)/gnome-calculator/{pkgver[:-2]}/gnome-calculator-{pkgver}.tar.xz"
sha256 = "2d36750a73890086122cf3f0c83e68517891585615165306fa1596a918668247"


@subpackage("gnome-calculator-devel")
def _(self):
    return self.default_devel()
