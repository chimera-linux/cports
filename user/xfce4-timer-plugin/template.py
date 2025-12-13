pkgname = "xfce4-timer-plugin"
pkgver = "1.8.0"
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
pkgdesc = "Xfce timer panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-timer-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-timer-plugin/{pkgver[:-2]}/xfce4-timer-plugin-{pkgver}.tar.xz"
sha256 = "1d3ac3aa2c4345400c025642778e7643aab41047622baf9cdc00bbac78e89f99"
