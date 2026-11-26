pkgname = "cinnamon-session"
pkgver = "6.6.4"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemd=disabled"]
hostmakedepends = ["glib-devel", "meson", "pkgconf"]
makedepends = [
    "cinnamon-desktop-devel",
    "elogind-devel",
    "glib-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libice-devel",
    "libsm-devel",
    "libx11-devel",
    "libxau-devel",
    "libxcomposite-devel",
    "libxext-devel",
    "libxrender-devel",
    "libxtst-devel",
    "mesa-devel",
    "pango-devel",
    "xapp-devel",
    "xtrans",
]
depends = [
    "cinnamon-desktop",
    "python-gobject",
    "python-setproctitle",
    "xapp",
]
pkgdesc = "Session manager for the Cinnamon desktop"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-session/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a5a2e5674671921f51f4dbbceb3cb2ac1088c0591c011078f75a214bcbfd641c"
options = ["!cross"]
