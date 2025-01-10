pkgname = "xfce4-time-out-plugin"
pkgver = "1.1.4"
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
    "xfce4-panel-devel",
]
pkgdesc = "Xfce time-out panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-time-out-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-time-out-plugin/{pkgver[:-2]}/xfce4-time-out-plugin-{pkgver}.tar.bz2"
sha256 = "b6b708900d7fd0cc3d8a045514962db94b60d959c266049aa2cff768fc381726"
