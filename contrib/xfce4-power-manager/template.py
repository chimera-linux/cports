pkgname = "xfce4-power-manager"
pkgver = "4.18.3"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxext-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxrandr-devel",
    "upower-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
depends = ["polkit"]
pkgdesc = "Xfce power manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/xfce/xfce4-power-manager/start"
source = f"$(XFCE_SITE)/xfce/xfce4-power-manager/{pkgver[:-2]}/xfce4-power-manager-{pkgver}.tar.bz2"
sha256 = "0d79dd0f68b90d07b384366be4d2291a6d7815410eb0c20d3d8e8590c62e84f0"
