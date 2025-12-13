pkgname = "xfce4-docklike-plugin"
pkgver = "0.5.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfce4windowing-devel",
    "libxi-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce taskbar panel plugin"
license = "GPL-3.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-docklike-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-docklike-plugin/{pkgver[:-2]}/xfce4-docklike-plugin-{pkgver}.tar.xz"
sha256 = "418aa01f51f6528d95ceeb3b19d52bdc0ac554447bdb7afa9975cca5234f244b"
