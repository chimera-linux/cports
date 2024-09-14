pkgname = "xfce4-fsguard-plugin"
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
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce free space guard panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-fsguard-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-fsguard-plugin/{pkgver[:-2]}/xfce4-fsguard-plugin-{pkgver}.tar.bz2"
sha256 = "84ef8bb4752292d64c0ef101badf7b14448790bfa0a85de644dbfa22986ec258"


def post_install(self):
    self.install_license("COPYING")
