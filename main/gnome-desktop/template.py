pkgname = "gnome-desktop"
pkgver = "43"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dudev=enabled", "-Dsystemd=disabled",]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel",
    "gettext-tiny", "docbook-xml", "itstool",
]
makedepends = [
    "eudev-devel", "gsettings-desktop-schemas-devel", "gtk+3-devel",
    "gtk4-devel", "gdk-pixbuf-devel", "libglib-devel", "fontconfig-devel",
    "libseccomp-devel", "libxkbcommon-devel", "iso-codes", "xkeyboard-config",
]
depends = [
    "bubblewrap", "gsettings-desktop-schemas", "iso-codes", "xkeyboard-config"
]
pkgdesc = "GNOME desktop management utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-desktop"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3d6e153317486157596aa3802f87676414c570738f450a94a041fe8835420a69"
# needs graphical environment
options = ["!check"]

@subpackage("gnome-desktop-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
