pkgname = "xfce4-timer-plugin"
pkgver = "1.7.3"
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
    "gtk+3-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce timer panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-timer-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-timer-plugin/{pkgver[:-2]}/xfce4-timer-plugin-{pkgver}.tar.bz2"
sha256 = "acf4c861af88608b9e802a76a4b05846bd30189e0085e826680cc179b6df4cd3"
