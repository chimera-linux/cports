pkgname = "xfce4-indicator-plugin"
pkgver = "2.5.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "ayatana-ido-devel",
    "gtk+3-devel",
    "libayatana-indicator-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce messaging menu panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-indicator-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-indicator-plugin/{pkgver[:-2]}/xfce4-indicator-plugin-{pkgver}.tar.xz"
sha256 = "e1a29a2c4837f53dd4825c51f0bd81da42cf36e6eec85d266d04c3d49511b451"
