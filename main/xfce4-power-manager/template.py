pkgname = "xfce4-power-manager"
pkgver = "4.18.4"
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
sha256 = "76918f7bdcd936dbbf20efd9221a33be0cd504c7d7ffce792bace3c720f3d874"
