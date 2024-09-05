pkgname = "gnome-calculator"
pkgver = "47_rc"
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
source = f"$(GNOME_SITE)/gnome-calculator/{pkgver[:2]}/gnome-calculator-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "0567eab5c810b0d3a0d60f570d48fcf8e3fe35bf34bbea33820edbf6f574148b"


@subpackage("gnome-calculator-devel")
def _(self):
    return self.default_devel()
