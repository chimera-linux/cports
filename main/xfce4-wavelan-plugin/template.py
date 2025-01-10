pkgname = "xfce4-wavelan-plugin"
pkgver = "0.6.4"
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
depends = ["network-manager-applet"]
pkgdesc = "Xfce WLAN stats panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-wavelan-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-wavelan-plugin/{pkgver[:-2]}/xfce4-wavelan-plugin-{pkgver}.tar.bz2"
sha256 = "129c917b40ffa10d96f3d2c0d03f1e8ad8037c79133e9a6436661e37dd7bb3de"


def post_install(self):
    self.install_license("COPYING")
