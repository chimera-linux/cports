pkgname = "xfce4-docklike-plugin"
pkgver = "0.4.2"
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
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce taskbar panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-docklike-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-docklike-plugin/{pkgver[:-2]}/xfce4-docklike-plugin-{pkgver}.tar.bz2"
sha256 = "b6a40b976a78f2abb1bec057c48d45bfb317e00b12e05a7dfcbea4d183f8db71"
