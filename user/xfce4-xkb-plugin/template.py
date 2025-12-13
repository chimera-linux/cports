pkgname = "xfce4-xkb-plugin"
pkgver = "0.9.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "garcon-devel",
    "gtk+3-devel",
    "libnotify-devel",
    "librsvg-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxklavier-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce keyboard layout panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-xkb-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-xkb-plugin/{pkgver[:-2]}/xfce4-xkb-plugin-{pkgver}.tar.xz"
sha256 = "7cd7f3626ef39dc4ce142b2f96ab7583cbea84b4c0352fbc9c9667faac0bdd12"
