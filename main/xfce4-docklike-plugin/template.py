pkgname = "xfce4-docklike-plugin"
pkgver = "0.4.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "cairo-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfce4windowing-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce taskbar panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-docklike-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-docklike-plugin/{pkgver[:-2]}/xfce4-docklike-plugin-{pkgver}.tar.bz2"
sha256 = "e81e16b4ab1c655a3202473d78cc81617bb4829e5dd102eecabf9addd7668a9d"
