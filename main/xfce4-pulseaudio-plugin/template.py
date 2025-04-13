pkgname = "xfce4-pulseaudio-plugin"
pkgver = "0.5.0"
pkgrel = 0
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
sha256 = "3fe69bc6f9c0dd68bd317c0a7813975cf162ba1dd64e23c2ffef372d4b4f808a"
