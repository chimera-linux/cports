pkgname = "xfce4-wavelan-plugin"
pkgver = "0.7.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
depends = ["network-manager-applet"]
pkgdesc = "Xfce WLAN stats panel plugin"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-wavelan-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-wavelan-plugin/{pkgver[:-2]}/xfce4-wavelan-plugin-{pkgver}.tar.xz"
sha256 = "5fdce1e1b0d29d0a258dca86bab9d4edcbc12098134b92e00ea1502086a49116"


def post_install(self):
    self.install_license("COPYING")
