pkgname = "xfce4-netload-plugin"
pkgver = "1.4.2"
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
    "xfce4-panel-devel",
]
pkgdesc = "Xfce network load panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-netload-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-netload-plugin/{pkgver[:-2]}/xfce4-netload-plugin-{pkgver}.tar.bz2"
sha256 = "a2041338408b2670f8debe57fcec6af539f704659eba853943c1524936ebabeb"
