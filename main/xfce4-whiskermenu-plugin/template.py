pkgname = "xfce4-whiskermenu-plugin"
pkgver = "2.8.4"
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
sha256 = "ed918950e01dc97fe831e01c698b44247f1537992999b1262ab61c799272b3b7"
