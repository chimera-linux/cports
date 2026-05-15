pkgname = "baobab"
pkgver = "50.0"
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
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/action/show/Apps/DiskUsageAnalyzer"
source = f"$(GNOME_SITE)/baobab/{pkgver[:-2]}/baobab-{pkgver}.tar.xz"
sha256 = "573c84f15f5f963a440500f6f43412c928ac2335f6b69dcb58f1a1fe5201024b"
hardening = ["vis", "!cfi"]
