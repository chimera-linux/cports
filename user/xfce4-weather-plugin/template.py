pkgname = "xfce4-weather-plugin"
pkgver = "0.12.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
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
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-weather-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-weather-plugin/{pkgver[:-2]}/xfce4-weather-plugin-{pkgver}.tar.xz"
sha256 = "5dd90b032c06ef4b64b818023154ef9463a2c694a0290e57f3412296c7545ff6"
