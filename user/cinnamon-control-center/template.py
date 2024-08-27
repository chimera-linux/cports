pkgname = "cinnamon-control-center"
pkgver = "6.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["gettext", "libxml2-progs", "meson", "pkgconf"]
makedepends = [
    "cinnamon-desktop-devel",
    "cinnamon-menus-devel",
    "colord-devel",
    "glib-devel",
    "gtk+3-devel",
    "iso-codes",
    "libgnomekbd-devel",
    "libgudev-devel",
    "libnma-devel",
    "libnotify-devel",
    "libwacom-devel",
    "libx11-devel",
    "libxi-devel",
    "libxklavier-devel",
    "modemmanager-devel",
    "networkmanager-devel",
    "polkit-devel",
    "upower-devel",
]
pkgdesc = "Collection of configuration plugins used in cinnamon-settings"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-control-center/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "44735f498fcd286cbb00c0e87a21caf9ed3c12033df61e5f2b4280c1327dea2a"


@subpackage("cinnamon-control-center-devel")
def _(self):
    return self.default_devel()
