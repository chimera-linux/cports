pkgname = "xfce4-weather-plugin"
pkgver = "0.11.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
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
sha256 = "65d40aff7863550858a9f9d2b6054f27c69a3e7e712991785987f9a73bba876b"
