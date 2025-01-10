pkgname = "xfce4-terminal"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = ["exo-devel", "libxfce4ui-devel", "vte-gtk3-devel"]
pkgdesc = "Xfce terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-terminal/start"
source = f"$(XFCE_SITE)/apps/xfce4-terminal/{pkgver[:-2]}/xfce4-terminal-{pkgver}.tar.bz2"
sha256 = "873c921da1f4b986ffb459d4960789c9c063af98648c9f0ca146dc6f6f5b71b7"
