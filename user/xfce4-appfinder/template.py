pkgname = "xfce4-appfinder"
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
    "garcon-devel",
    "glib-devel",
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce application finder"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfce4-appfinder/start"
source = f"$(XFCE_SITE)/xfce/xfce4-appfinder/{pkgver[:-2]}/xfce4-appfinder-{pkgver}.tar.bz2"
sha256 = "82ca82f77dc83e285db45438c2fe31df445148aa986ffebf2faabee4af9e7304"
