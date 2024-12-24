pkgname = "xfce4-indicator-plugin"
pkgver = "2.4.3"
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
    "ayatana-ido-devel",
    "gtk+3-devel",
    "libayatana-indicator-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce messaging menu panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-indicator-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-indicator-plugin/{pkgver[:-2]}/xfce4-indicator-plugin-{pkgver}.tar.bz2"
sha256 = "4fd9fe74b3ef0ea1fb6d2b2507873108052f4f532b609e3297321dbf3a52d2db"
