pkgname = "orage"
pkgver = "4.20.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-x11-tray-icon"]
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
    "libical-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
]
pkgdesc = "Xfce time-managing app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/orage/start"
source = f"$(XFCE_SITE)/apps/orage/{pkgver[:-2]}/orage-{pkgver}.tar.bz2"
sha256 = "ee07918a6f6033e6107e9c1b8e164c645ea590ffbdba0b58d071c0e491046a85"
