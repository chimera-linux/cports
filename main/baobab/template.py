pkgname = "baobab"
pkgver = "47.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "Graphical directory tree analyzer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/action/show/Apps/DiskUsageAnalyzer"
source = f"$(GNOME_SITE)/baobab/{pkgver[:-2]}/baobab-{pkgver}.tar.xz"
sha256 = "b88f74f9c052d3c2388f7062d228cf5e927545acf7408c56841df80ccd1f9c37"
hardening = ["vis", "!cfi"]
