pkgname = "xfce4-eyes-plugin"
pkgver = "4.6.2"
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
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce eyes panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-eyes-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-eyes-plugin/{pkgver[:-2]}/xfce4-eyes-plugin-{pkgver}.tar.bz2"
sha256 = "02b4ac637604a0b9262616cb9613e0fe6797fb6b0f1fc2889a77e1e0ad4a01a5"
