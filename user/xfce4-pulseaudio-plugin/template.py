pkgname = "xfce4-pulseaudio-plugin"
pkgver = "0.5.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "exo-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libkeybinder3-devel",
    "libnotify-devel",
    "libpulse-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfce4windowing-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
# Default mixer
depends = ["pavucontrol"]
pkgdesc = "Xfce pulseaudio panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-pulseaudio-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-pulseaudio-plugin/{pkgver[:-2]}/xfce4-pulseaudio-plugin-{pkgver}.tar.xz"
sha256 = "8e1f3a505f37aa3bc2816a58bec5f9555366f1c476f10eab59fd0e6581d08c47"
