pkgname = "xfce4-timer-plugin"
pkgver = "1.7.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "gtk+3-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce timer panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-timer-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-timer-plugin/{pkgver[:-2]}/xfce4-timer-plugin-{pkgver}.tar.bz2"
sha256 = "feb3b8c2d39505e816683540a3226bd7bda870ccbcb4c7d0f6abfeeff5c58b7d"
