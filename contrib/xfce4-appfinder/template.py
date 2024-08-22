pkgname = "xfce4-appfinder"
pkgver = "4.18.1"
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
    "garcon-devel",
    "glib-devel",
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce application finder"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfce4-appfinder/start"
source = f"$(XFCE_SITE)/xfce/xfce4-appfinder/{pkgver[:-2]}/xfce4-appfinder-{pkgver}.tar.bz2"
sha256 = "9854ea653981be544ad545850477716c4c92d0c43eb47b75f78534837c0893f9"
