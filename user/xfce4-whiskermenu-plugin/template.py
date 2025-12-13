pkgname = "xfce4-whiskermenu-plugin"
pkgver = "2.10.0"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
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
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-whiskermenu-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-whiskermenu-plugin/{pkgver[:-2]}/xfce4-whiskermenu-plugin-{pkgver}.tar.xz"
sha256 = "c2efb3782816d44d421dcbee2900b9513bdb2469b695b776641f495601f33a10"
