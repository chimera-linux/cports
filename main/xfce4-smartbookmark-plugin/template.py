pkgname = "xfce4-smartbookmark-plugin"
pkgver = "0.5.3"
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
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce browser search panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-smartbookmark-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-smartbookmark-plugin/{pkgver[:-2]}/xfce4-smartbookmark-plugin-{pkgver}.tar.bz2"
sha256 = "3b4db0ac198339197a7682935f0bba5a7e8dd7f35bf575ac6665afa4cecec236"
