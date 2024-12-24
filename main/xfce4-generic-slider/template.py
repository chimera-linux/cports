pkgname = "xfce4-generic-slider"
pkgver = "1.0.1"
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
pkgdesc = "Xfce generic slider panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-only"
url = "https://docs.xfce.org/panel-plugins/xfce4-generic-slider/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-generic-slider/{pkgver[:-2]}/xfce4-generic-slider-{pkgver}.tar.bz2"
sha256 = "5f3f1da2fa1428ddc51dbbdcdf119f88b023260b605edd3d1d796261a047f0ec"
