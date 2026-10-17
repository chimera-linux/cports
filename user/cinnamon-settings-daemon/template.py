pkgname = "cinnamon-settings-daemon"
pkgver = "6.6.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["glib-devel", "meson", "pkgconf"]
makedepends = [
    "cinnamon-desktop-devel",
    "colord-devel",
    "cups-devel",
    "elogind-devel",
    "fontconfig-devel",
    "glib-devel",
    "gtk+3-devel",
    "lcms2-devel",
    "libcanberra-devel",
    "libgudev-devel",
    "libnotify-devel",
    "librsvg-devel",
    "libwacom-devel",
    "libx11-devel",
    "libxext-devel",
    "libxi-devel",
    "nss-devel",
    "pango-devel",
    "polkit-devel",
    "upower-devel",
]
pkgdesc = "Settings daemon for the Cinnamon desktop"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-settings-daemon/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "215006afe3e59e4998fd3bb9f8ecf1b7c926a08b5398b42e482c5008483c970a"
options = ["etcfiles", "!cross"]


def post_install(self):
    # internal helper library, nothing links to it
    self.uninstall("usr/lib/cinnamon-settings-daemon-3.0")
