pkgname = "xfce4-session"
pkgver = "4.20.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "iceauth",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libsm-devel",
    "libwnck-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfce4windowing-devel",
    "polkit-devel",
    "xfconf-devel",
]
depends = ["iceauth"]
pkgdesc = "Xfce desktop session"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfce4-session/start"
source = f"$(XFCE_SITE)/xfce/xfce4-session/{pkgver[:-2]}/xfce4-session-{pkgver}.tar.bz2"
sha256 = "5229233fe6ee692361cc28724886c5b08e0216d89f09c42d273191d38fd64f85"
