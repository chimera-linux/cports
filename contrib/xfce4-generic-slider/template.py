pkgname = "xfce4-generic-slider"
pkgver = "1.0.0"
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
    "gtk+3-devel",
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce generic slider panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-only"
url = "https://docs.xfce.org/panel-plugins/xfce4-generic-slider/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-generic-slider/{pkgver[:-2]}/xfce4-generic-slider-{pkgver}.tar.bz2"
sha256 = "06074d1123c1767bd0e25c6e7b34ade0a1e9edf51c996b8a643772e5881024bb"
