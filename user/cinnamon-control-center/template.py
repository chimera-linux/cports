pkgname = "cinnamon-control-center"
pkgver = "6.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["gettext", "meson", "pkgconf"]
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
sha256 = "f3e5caf03c4d629fbaf883caa816fe799685438d650012621e51457583000d07"


@subpackage("cinnamon-control-center-devel")
def _(self):
    return self.default_devel()
