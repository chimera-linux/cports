pkgname = "xfce4-netload-plugin"
pkgver = "1.4.1"
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
    "xfce4-panel-devel",
]
pkgdesc = "Xfce network load panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-netload-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-netload-plugin/{pkgver[:-2]}/xfce4-netload-plugin-{pkgver}.tar.bz2"
sha256 = "9fac3a3ad52e18584bfb127cd1721d56de1004b9fdd140915fded89704ccb44e"
