pkgname = "xfce4-power-manager"
pkgver = "4.20.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
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
license = "GPL-2.0-only"
url = "https://docs.xfce.org/xfce/xfce4-power-manager/start"
source = f"$(XFCE_SITE)/xfce/xfce4-power-manager/{pkgver[:-2]}/xfce4-power-manager-{pkgver}.tar.bz2"
sha256 = "971391cef63352833bdd92df28957392e17e1f2b3d486c0f57294fd204d6ed29"
