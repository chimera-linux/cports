pkgname = "xfce4-pulseaudio-plugin"
pkgver = "0.4.9"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-pulseaudio-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-pulseaudio-plugin/{pkgver[:-2]}/xfce4-pulseaudio-plugin-{pkgver}.tar.bz2"
sha256 = "a0807615fb2848d0361b7e4568a44f26d189fda48011c7ba074986c8bfddc99a"
