pkgname = "xfce4-clipman-plugin"
pkgver = "1.7.0"
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
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxtst-devel",
    "qrencode-devel",
    "wayland-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
    "xorgproto",
]
pkgdesc = "Xfce clipboard manager app and panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-clipman-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-clipman-plugin/{pkgver[:-2]}/xfce4-clipman-plugin-{pkgver}.tar.xz"
sha256 = "903302c3070a951d44ee17a84fa3cf21d36c6787678af8fbfc79e469fd00cb46"
