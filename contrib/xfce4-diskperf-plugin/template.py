pkgname = "xfce4-diskperf-plugin"
pkgver = "2.7.0"
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
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce disk performance panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-diskperf-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-diskperf-plugin/{pkgver[:-2]}/xfce4-diskperf-plugin-{pkgver}.tar.bz2"
sha256 = "5909a65341a6af4d7ff3c7bb87aeac91c763f69b43ae9dc4a10668ac226fecc9"


def post_install(self):
    self.install_license("COPYING")
