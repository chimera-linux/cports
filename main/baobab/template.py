pkgname = "baobab"
pkgver = "49.0"
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
sha256 = "195c0182dc4d7f694dd0b4ee36e72e0f4ab757825fc238233409eec2df483fae"
hardening = ["vis", "!cfi"]
