pkgname = "baobab"
pkgver = "42.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala", "itstool"
]
makedepends = [
    "gtk4-devel", "libglib-devel", "libadwaita-devel",
]
depends = ["hicolor-icon-theme", "gsettings-desktop-schemas"]
pkgdesc = "Graphical directory tree analyzer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/action/show/Apps/DiskUsageAnalyzer"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4b1aabe6bab1582b3fea79a2829bce7f2415bb6e5062f25357aeedd5317a50dc"
