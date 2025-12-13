pkgname = "xfce4-terminal"
pkgver = "1.1.5"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "exo-devel",
    "glib-devel",
    "gtk-layer-shell-devel",
    "libxfce4ui-devel",
    "vte-gtk3-devel",
]
pkgdesc = "Xfce terminal emulator"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-terminal/start"
source = f"$(XFCE_SITE)/apps/xfce4-terminal/{pkgver[:-2]}/xfce4-terminal-{pkgver}.tar.xz"
sha256 = "3c5b1d3a01a9a113852ac0f77d1c85bf3a356b43de33ec805b21ceca7d6f0a63"
