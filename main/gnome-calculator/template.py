pkgname = "gnome-calculator"
pkgver = "49.1.1"
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
sha256 = "840d3459ed69f2787a9669f96f6b3f9eff16cb486900c719ac252c424563463d"


@subpackage("gnome-calculator-devel")
def _(self):
    return self.default_devel()
