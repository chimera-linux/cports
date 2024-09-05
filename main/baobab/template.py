pkgname = "baobab"
pkgver = "47_alpha"
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
source = f"$(GNOME_SITE)/baobab/{pkgver[:2]}/baobab-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "d36715445809ea11a2ad2970cea80b35d9d1a7271f08049654279b474821451c"
hardening = ["vis", "!cfi"]
