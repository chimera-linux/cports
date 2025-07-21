pkgname = "gnome-calculator"
pkgver = "48.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Ddefault_library=shared",
]
hostmakedepends = [
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
sha256 = "bc4bd41a9ba190f45cbee0d8c6752cdc5d28b0cef1c6bd0c01e2dae1f3c19162"


@subpackage("gnome-calculator-devel")
def _(self):
    return self.default_devel()
