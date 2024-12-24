pkgname = "xfce4-places-plugin"
pkgver = "1.8.4"
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
    "exo-devel",
    "gtk+3-devel",
    "libnotify-devel",
    "libwnck-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce folders and media quick access panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-places-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-places-plugin/{pkgver[:-2]}/xfce4-places-plugin-{pkgver}.tar.bz2"
sha256 = "ba766a5d31580fad043fbd1fd66b811cbda706229473d24a734a590d49ef710e"
