pkgname = "thunar-volman"
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
    "exo-devel",
    "glib-devel",
    "gtk+3-devel",
    "libgudev-devel",
    "libnotify-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfconf-devel",
]
pkgdesc = "Thunar volume manager extension"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/xfce/thunar/thunar-volman"
source = f"$(XFCE_SITE)/xfce/thunar-volman/{pkgver[:-2]}/thunar-volman-{pkgver}.tar.bz2"
sha256 = "b0dad852959b515b8fbfd1ed552e362340347d26d5246e7f1b973027131eb1da"
