pkgname = "gnome-desktop"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dudev=enabled",
    "-Dsystemd=disabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "gettext-tiny",
    "docbook-xml",
    "itstool",
]
makedepends = [
    "udev-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "fontconfig-devel",
    "libseccomp-devel",
    "libxkbcommon-devel",
    "iso-codes",
    "xkeyboard-config",
]
depends = [
    "bubblewrap",
    "gsettings-desktop-schemas",
    "iso-codes",
    "xkeyboard-config",
]
pkgdesc = "GNOME desktop management utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-desktop"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "42c773745d84ba14bc1cf1c4c6f4606148803a5cd337941c63964795f3c59d42"
# needs graphical environment
options = ["!check"]


@subpackage("gnome-desktop-devel")
def _devel(self):
    return self.default_devel()
