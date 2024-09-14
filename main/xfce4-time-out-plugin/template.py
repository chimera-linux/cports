pkgname = "xfce4-time-out-plugin"
pkgver = "1.1.3"
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
    "xfce4-panel-devel",
]
pkgdesc = "Xfce time-out panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-time-out-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-time-out-plugin/{pkgver[:-2]}/xfce4-time-out-plugin-{pkgver}.tar.bz2"
sha256 = "5a1ca36361e95ec718bbd887ea5be6a270ab458d1c2d672186721522a7228ee8"
