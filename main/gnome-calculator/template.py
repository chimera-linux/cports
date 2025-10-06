pkgname = "gnome-calculator"
pkgver = "49.0.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
sha256 = "ecbe20e630575fb8bc23790d35f386ac1779003c40dc5c877d3cd2da0fc7453f"


@subpackage("gnome-calculator-devel")
def _(self):
    return self.default_devel()
