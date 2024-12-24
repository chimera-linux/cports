pkgname = "xfce4-clipman-plugin"
pkgver = "1.6.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-clipman-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-clipman-plugin/{pkgver[:-2]}/xfce4-clipman-plugin-{pkgver}.tar.bz2"
sha256 = "9bae27808a50e959e0912b7202ea5d651ed7401a6fc227f811d9bdaf2e44178c"
