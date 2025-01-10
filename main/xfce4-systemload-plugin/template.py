pkgname = "xfce4-systemload-plugin"
pkgver = "1.3.3"
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
    "libgtop-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "upower-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce system load panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later AND BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-systemload-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-systemload-plugin/{pkgver[:-2]}/xfce4-systemload-plugin-{pkgver}.tar.bz2"
sha256 = "6852d5d9c9a74d0e0db582c6f5fe7390ebe48a2eb5692177ae12e1c4ccc6efc9"


def post_install(self):
    self.install_license("COPYING")
