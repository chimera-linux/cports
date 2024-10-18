pkgname = "cinnamon-desktop"
pkgver = "6.2.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dpnp_ids=/usr/share/hwdata/pnp.ids"]
hostmakedepends = ["gettext", "gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "elogind-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk+3-devel",
    "libpulse-devel",
    "libx11-devel",
    "libxext-devel",
    "libxkbfile-devel",
    "libxrandr-devel",
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
sha256 = "95bb6fc16597601b1febde4bd1317ba9c3ab662119b6b8e602b49e832d3f3eb7"
options = ["!cross"]


@subpackage("cinnamon-desktop-devel")
def _(self):
    return self.default_devel()
