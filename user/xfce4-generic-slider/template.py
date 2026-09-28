pkgname = "xfce4-generic-slider"
pkgver = "1.1.0"
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
    "xfce4-panel-devel",
]
pkgdesc = "Xfce generic slider panel plugin"
license = "GPL-3.0-only"
url = "https://docs.xfce.org/panel-plugins/xfce4-generic-slider/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-generic-slider/{pkgver[:-2]}/xfce4-generic-slider-{pkgver}.tar.xz"
sha256 = "0cef3174157621e14d123a9d246ee3b1d7c8ef89579377398305a4eb33636f5f"
