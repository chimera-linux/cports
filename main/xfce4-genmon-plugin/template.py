pkgname = "xfce4-genmon-plugin"
pkgver = "4.2.0"
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
sha256 = "948d08ee5f2140847f109b531bc1d4cc6268496913ea7600d3c5ad89025a0362"
