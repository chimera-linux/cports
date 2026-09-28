pkgname = "xfce4-stopwatch-plugin"
pkgver = "0.6.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce stopwatch panel plugin"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-stopwatch-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-stopwatch-plugin/{pkgver[:-2]}/xfce4-stopwatch-plugin-{pkgver}.tar.xz"
sha256 = "9be4825f6dc3b5227ba3c71b345da4159ac3364f659784b57845bb06cf31ef43"


def post_install(self):
    self.install_license("COPYING")
