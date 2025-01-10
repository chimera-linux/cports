pkgname = "xfce4-genmon-plugin"
pkgver = "4.2.1"
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
    "xfconf-devel",
]
pkgdesc = "Xfce generic program monitor panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-genmon-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-genmon-plugin/{pkgver[:-2]}/xfce4-genmon-plugin-{pkgver}.tar.bz2"
sha256 = "de540562e1ea58f35a9c815e20736d26af541a0a9372011148cb75b5f0b65951"
