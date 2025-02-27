pkgname = "gnome-desktop"
pkgver = "44.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dudev=enabled",
    "-Dsystemd=disabled",
]
hostmakedepends = [
    "docbook-xml",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "fontconfig-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "iso-codes",
    "libseccomp-devel",
    "libxkbcommon-devel",
    "udev-devel",
    "xkeyboard-config",
]
depends = [
    "bubblewrap",
    "gsettings-desktop-schemas",
    "iso-codes",
    "xkeyboard-config",
]
pkgdesc = "GNOME desktop management utilities"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-desktop"
source = (
    f"$(GNOME_SITE)/gnome-desktop/{pkgver[:-2]}/gnome-desktop-{pkgver}.tar.xz"
)
sha256 = "ae7ca55dc9e08914999741523a17d29ce223915626bd2462a120bf96f47a79ab"
# needs graphical environment
options = ["!check", "!cross"]


@subpackage("gnome-desktop-devel")
def _(self):
    return self.default_devel()
