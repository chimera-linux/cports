pkgname = "cinnamon-control-center"
pkgver = "6.6.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["gettext", "glib-devel", "meson", "pkgconf"]
makedepends = [
    "cinnamon-desktop-devel",
    "cinnamon-menus-devel",
    "colord-devel",
    "glib-devel",
    "gtk+3-devel",
    "libgudev-devel",
    "libnma-devel",
    "libnotify-devel",
    "libwacom-devel",
    "libx11-devel",
    "libxi-devel",
    "modemmanager-devel",
    "networkmanager-devel",
    "polkit-devel",
    "upower-devel",
]
pkgdesc = "Configuration panels for the Cinnamon desktop"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-control-center/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2de5fbc5a9fcc2e1dad9c595dfb1d9047ff885d391f45d6ffe8b6711bb4e24e4"
options = ["!cross"]


@subpackage("cinnamon-control-center-devel")
def _(self):
    return self.default_devel()
