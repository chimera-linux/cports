pkgname = "gnome-calculator"
pkgver = "51.0"
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
sha256 = "5bfb4c53eec61feb6c03faf85218804e87413ecb647e08fde6379bf2b1839190"


@subpackage("gnome-calculator-devel")
def _(self):
    return self.default_devel()
