pkgname = "xfce4-fsguard-plugin"
pkgver = "1.1.4"
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
sha256 = "24b3789be6de92678e7036678530c4da4b3838aa3cda428439aa8d140704a4a6"


def post_install(self):
    self.install_license("COPYING")
