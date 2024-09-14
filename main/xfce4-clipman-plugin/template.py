pkgname = "xfce4-clipman-plugin"
pkgver = "1.6.6"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
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
sha256 = "08ad475b006f878df5dd20d83c98edc33ed21e69b414d0e5ff6d4accd64d7120"
