pkgname = "xfce4-mixer"
pkgver = "4.18.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libkeybinder3-devel",
    "libpulse-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce volume control app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-mixer/start"
source = (
    f"$(XFCE_SITE)/apps/xfce4-mixer/{pkgver[:-2]}/xfce4-mixer-{pkgver}.tar.bz2"
)
sha256 = "b27f67dccc9dd67d989b405dab02be1299436dd71b58edb88a1d5f82571ead95"
