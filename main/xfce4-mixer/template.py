pkgname = "xfce4-mixer"
pkgver = "4.18.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "pkgconf",
    "slibtool",
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
sha256 = "101580c15bfe7fe430a149da3603357558b7d0a66258dfdb78d04c1bf3c791a1"
