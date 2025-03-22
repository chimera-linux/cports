pkgname = "gnome-calculator"
pkgver = "48.0.2"
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
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calculator"
source = f"$(GNOME_SITE)/gnome-calculator/{pkgver[:-4]}/gnome-calculator-{pkgver}.tar.xz"
sha256 = "a4cdbab35be24bb4017359b99ffcb6c8afc00848291ad7a4720e6ca075700dc4"


@subpackage("gnome-calculator-devel")
def _(self):
    return self.default_devel()
