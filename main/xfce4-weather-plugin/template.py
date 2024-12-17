pkgname = "xfce4-weather-plugin"
pkgver = "0.11.3"
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
    "json-c-devel",
    "libsoup-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxml2-devel",
    "upower-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce weather panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-weather-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-weather-plugin/{pkgver[:-2]}/xfce4-weather-plugin-{pkgver}.tar.bz2"
sha256 = "002d1fe63906d2f3a012f3cb58cceff1dfbcc466759e36c76d3b03dd01c0dc57"
