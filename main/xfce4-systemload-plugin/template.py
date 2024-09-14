pkgname = "xfce4-systemload-plugin"
pkgver = "1.3.2"
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
sha256 = "bb303fc3020e053ad1fa0b8fcbf0d7681c5563bb8f649357d6a95a577802b072"


def post_install(self):
    self.install_license("COPYING")
