pkgname = "thunar-archive-plugin"
pkgver = "0.6.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "libxfce4ui-devel",
    "thunar-devel",
]
pkgdesc = "Xfce file manager"
license = "LGPL-2.0-only"
url = "https://docs.xfce.org/xfce/thunar/start"
source = f"$(XFCE_SITE)/thunar-plugins/thunar-archive-plugin/{pkgver[: pkgver.rfind('.')]}/thunar-archive-plugin-{pkgver}.tar.xz"
sha256 = "692708cd047c7a552f2f85fe2ee32f19c7d5be5bf695d0288e8cadf50289db06"
