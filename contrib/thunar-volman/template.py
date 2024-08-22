pkgname = "thunar-volman"
pkgver = "4.18.0"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/xfce/thunar/thunar-volman"
source = f"$(XFCE_SITE)/xfce/thunar-volman/{pkgver[:-2]}/thunar-volman-{pkgver}.tar.bz2"
sha256 = "93b75c7ffbe246a21f4190295acc148e184be8df397e431b258d0d676e87fc65"
