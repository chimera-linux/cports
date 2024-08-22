pkgname = "xfce4-wavelan-plugin"
pkgver = "0.6.3"
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
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
depends = ["network-manager-applet"]
pkgdesc = "Xfce WLAN stats panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-wavelan-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-wavelan-plugin/{pkgver[:-2]}/xfce4-wavelan-plugin-{pkgver}.tar.bz2"
sha256 = "61c0c2f56cb70872d403b770dd76349df9ff24c0dbe905ee1b4f913c34d8f72b"


def post_install(self):
    self.install_license("COPYING")
