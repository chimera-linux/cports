pkgname = "cinnamon-desktop"
pkgver = "6.4.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dpnp_ids=/usr/share/hwdata/pnp.ids"]
hostmakedepends = ["gettext", "gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "elogind-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk+3-devel",
    "iso-codes",
    "libpulse-devel",
    "libx11-devel",
    "libxext-devel",
    "libxkbfile-devel",
    "libxrandr-devel",
    "udev-devel",
    "xkeyboard-config",
]
depends = [
    "adwaita-icon-theme",
    "adwaita-icon-theme-legacy",
    "chimera-artwork",
    "hwdata-pnp",
]
pkgdesc = "Cinnamon desktop library and common settings schemas"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-desktop/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "61d2fb8a8b2e9eac66522ff78ece2cdc63c6083895a4823642c6f3c06bf83c51"
options = ["!cross"]


@subpackage("cinnamon-desktop-devel")
def _(self):
    return self.default_devel()
