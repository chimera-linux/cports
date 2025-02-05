pkgname = "gnome-calculator"
pkgver = "47.1"
pkgrel = 0
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
    "gtk+3-update-icon-cache",
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
sha256 = "be9f922799b7e7e65c97348b9b7e647ffe33c831bb3a51d39e2c168d2adc40e0"


@subpackage("gnome-calculator-devel")
def _(self):
    return self.default_devel()
