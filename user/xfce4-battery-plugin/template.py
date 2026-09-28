pkgname = "xfce4-battery-plugin"
pkgver = "1.2.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "gettext", "pkgconf"]
makedepends = [
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce battery panel plugin"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-battery-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-battery-plugin/{pkgver[:-2]}/xfce4-battery-plugin-{pkgver}.tar.xz"
sha256 = "1dba8f470d2b12517e7b86d83cd2ebf13eb57ff1a01a4f2d2d156cf5194d97b6"
