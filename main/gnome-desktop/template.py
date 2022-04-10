pkgname = "gnome-desktop"
pkgver = "42.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgnome_distributor=Chimera",
    "-Dudev=enabled",
    "-Dsystemd=disabled",
    "-Ddate_in_gnome_version=false",
]
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f3caa293a5e86f6ccad18f817273db1c67061e680d79d839aa8a7528e5bb26d6"
# needs graphical environment
options = ["!check"]

@subpackage("gnome-desktop-devel")
def _devel(self):
    return self.default_devel()
