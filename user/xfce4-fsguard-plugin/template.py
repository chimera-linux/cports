pkgname = "xfce4-fsguard-plugin"
pkgver = "1.2.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce free space guard panel plugin"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-fsguard-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-fsguard-plugin/{pkgver[:-2]}/xfce4-fsguard-plugin-{pkgver}.tar.xz"
sha256 = "9e40cf3ce7b34e1c27d6b442f3a067886c35154b5d0c4d644a239038611da64f"


def post_install(self):
    self.install_license("COPYING")
