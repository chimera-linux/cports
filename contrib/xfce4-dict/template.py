pkgname = "xfce4-dict"
pkgver = "0.8.6"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gmake",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce dictionary search app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-dict/start"
source = (
    f"$(XFCE_SITE)/apps/xfce4-dict/{pkgver[:-2]}/xfce4-dict-{pkgver}.tar.bz2"
)
sha256 = "ae5db7ca70354d3293fc08eaf7ca40cdbc91799a219f199d824684b39e6c0a41"
