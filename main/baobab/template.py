pkgname = "baobab"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala", "itstool"
]
makedepends = [
    "gtk4-devel", "glib-devel", "libadwaita-devel",
]
depends = ["hicolor-icon-theme", "gsettings-desktop-schemas"]
pkgdesc = "Graphical directory tree analyzer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/action/show/Apps/DiskUsageAnalyzer"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "52c6864118f5697f5a5736882dcda27db22e7220bc492838deecc699246cdb26"
# FIXME cfi
hardening = ["vis", "!cfi"]
