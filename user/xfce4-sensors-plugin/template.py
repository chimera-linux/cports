pkgname = "xfce4-sensors-plugin"
pkgver = "1.5.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dprocacpi=disabled", "-Dsysfsacpi=enabled"]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libnotify-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "lm-sensors-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce hardware sensors panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-sensors-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-sensors-plugin/{pkgver[:-2]}/xfce4-sensors-plugin-{pkgver}.tar.xz"
sha256 = "840442b87fdddcd8595bd9f83ea8b81f771fe296bb9d2abf0e1979e208727ae9"
