pkgname = "xfce4-diskperf-plugin"
pkgver = "2.7.1"
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
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce disk performance panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-diskperf-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-diskperf-plugin/{pkgver[:-2]}/xfce4-diskperf-plugin-{pkgver}.tar.bz2"
sha256 = "dd5f521cc4ab40a42958dcf59b6bec5da8fafacf71f3266971942e25b43af8ae"


def post_install(self):
    self.install_license("COPYING")
