pkgname = "baobab"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala", "itstool",
    "desktop-file-utils",
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
sha256 = "845b63bb9123d74568c8126c571bbc74273483ff920179a2cf1eddbbefa1bfc0"
# FIXME cfi
hardening = ["vis", "!cfi"]
