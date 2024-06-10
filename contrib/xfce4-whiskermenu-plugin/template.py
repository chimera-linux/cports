pkgname = "xfce4-whiskermenu-plugin"
pkgver = "2.8.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "gettext",
    "pkgconf",
]
makedepends = [
    "accountsservice-devel",
    "exo-devel",
    "garcon-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce application launcher panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-whiskermenu-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-whiskermenu-plugin/{pkgver[:-2]}/xfce4-whiskermenu-plugin-{pkgver}.tar.bz2"
sha256 = "e776c287658f98d0739447279522fe78766088438242cf2365a49c8973fc9cd0"
