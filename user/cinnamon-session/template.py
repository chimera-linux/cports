pkgname = "cinnamon-session"
pkgver = "6.2.1"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib"]
hostmakedepends = ["meson", "pkgconf"]
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
depends = ["gtk+3", "python-gobject", "python-setproctitle", "xapp"]
pkgdesc = "Cinnamon session manager"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-session/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "69d39494201f2cd7e30d880813df69ddeef143befc660ed953683d5ddac6153f"
hardening = ["vis"]
