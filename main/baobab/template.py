pkgname = "baobab"
pkgver = "45.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "vala",
    "itstool",
    "desktop-file-utils",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "libadwaita-devel",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "Graphical directory tree analyzer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/action/show/Apps/DiskUsageAnalyzer"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a7d2cf308a6c839ee0b0bf074f8f5fd60d62ae2f064a94b3c610d6560b758e86"
# FIXME cfi
hardening = ["vis", "!cfi"]

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
