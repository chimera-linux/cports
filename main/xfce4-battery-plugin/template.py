pkgname = "xfce4-battery-plugin"
pkgver = "1.1.6"
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
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce battery panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-battery-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-battery-plugin/{pkgver[:-2]}/xfce4-battery-plugin-{pkgver}.tar.bz2"
sha256 = "327d7304dded8411cd1a48da4f46bac248b44d8b27ffbc2036e0268cb37c3676"
