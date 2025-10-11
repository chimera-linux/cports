pkgname = "cinnamon-desktop"
pkgver = "6.4.2"
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
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-desktop/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f11d063c7ecb86b98803e9a22ade0655d979b334f6c90fdd1cc6f50bbe6e9992"
options = ["!cross"]


@subpackage("cinnamon-desktop-devel")
def _(self):
    return self.default_devel()
