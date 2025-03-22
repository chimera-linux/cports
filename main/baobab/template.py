pkgname = "baobab"
pkgver = "48.0"
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
sha256 = "54592504d49d807f23591be7e7eef10c6c9dfcb7ac527b81c3acd58787b26fda"
hardening = ["vis", "!cfi"]
