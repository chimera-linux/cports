pkgname = "xfce4-windowck-plugin"
pkgver = "0.6.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
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
    "xfconf-devel",
]
pkgdesc = "Xfce window controls/title bar panel plugin"
license = "GPL-3.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-windowck-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-windowck-plugin/{pkgver[:-2]}/xfce4-windowck-plugin-{pkgver}.tar.xz"
sha256 = "032e305d74f17bd65b28bd260cf192fcf8aa0df33d116087e485fd1368b7cf39"
