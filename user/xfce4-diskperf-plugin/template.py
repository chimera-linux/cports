pkgname = "xfce4-diskperf-plugin"
pkgver = "2.8.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce disk performance panel plugin"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-diskperf-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-diskperf-plugin/{pkgver[:-2]}/xfce4-diskperf-plugin-{pkgver}.tar.xz"
sha256 = "3833920a3a4a81b3c676c4fab6dd178f4a222d66f316a0783a9149a0153b7fb6"


def post_install(self):
    self.install_license("COPYING")
