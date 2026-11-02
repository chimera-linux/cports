pkgname = "gnome-calculator"
pkgver = "51.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
]
hostmakedepends = [
    "blueprint-compiler",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "gtksourceview-devel",
    "libadwaita-devel",
    "libgee-devel",
    "libsoup-devel",
    "mpc-devel",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "GNOME calculator"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calculator"
source = f"$(GNOME_SITE)/gnome-calculator/{pkgver[:2]}/gnome-calculator-{pkgver}.tar.xz"
sha256 = "03edf5972adc020b7e872233caba42f759e9879fc4b96f014580f136179c4fa0"


@subpackage("gnome-calculator-devel")
def _(self):
    return self.default_devel()
