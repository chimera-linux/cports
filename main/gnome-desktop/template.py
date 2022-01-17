pkgname = "gnome-desktop"
pkgver = "41.3"
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
    "gdk-pixbuf-devel", "libglib-devel", "fontconfig-devel",
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
sha256 = "8cd1caab9311828c0452468c6a5067a9bc4463835b23a14be44e8fd9b03001c6"
# needs graphical environment
options = ["!check"]

@subpackage("gnome-desktop-devel")
def _devel(self):
    return self.default_devel()
