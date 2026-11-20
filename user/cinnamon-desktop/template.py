pkgname = "cinnamon-desktop"
pkgver = "6.6.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemd=disabled"]
hostmakedepends = ["gettext", "gobject-introspection", "meson", "pkgconf"]
makedepends = [
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
]
pkgdesc = "Cinnamon desktop library and common settings schemas"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-desktop/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4ed0d52a072551c6d536f1be68d4fcdb4166454fc9e48567ab2550282086b0f4"
options = ["!cross"]


@subpackage("cinnamon-desktop-devel")
def _(self):
    return self.default_devel()
