pkgname = "xfce4-xkb-plugin"
pkgver = "0.8.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "garcon-devel",
    "gtk+3-devel",
    "libnotify-devel",
    "librsvg-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxklavier-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce keyboard layout panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-xkb-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-xkb-plugin/{pkgver[:-2]}/xfce4-xkb-plugin-{pkgver}.tar.bz2"
sha256 = "86ce4a194c47c506315cfded3a041067a72dedcb6d9cc2f9c99853203d332b19"
