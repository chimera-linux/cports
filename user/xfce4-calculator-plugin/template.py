pkgname = "xfce4-calculator-plugin"
pkgver = "0.8.0"
pkgrel = 2
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
pkgdesc = "Xfce calculator panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-calculator-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-calculator-plugin/{pkgver[:-2]}/xfce4-calculator-plugin-{pkgver}.tar.xz"
sha256 = "aaf3d7e9654ef6cf8ec442ad9e4316c481f9a6087a8e8949261140f5ae136aeb"
