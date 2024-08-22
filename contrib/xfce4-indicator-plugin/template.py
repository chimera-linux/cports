pkgname = "xfce4-indicator-plugin"
pkgver = "2.4.2"
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
    "ayatana-ido-devel",
    "gtk+3-devel",
    "libayatana-indicator-devel",
    "libx11-devel",
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
sha256 = "4f50364e4db2993a036244dc18540b061637515ad127769b67d8f7301e2eaa1a"
