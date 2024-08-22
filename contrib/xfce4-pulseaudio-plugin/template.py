pkgname = "xfce4-pulseaudio-plugin"
pkgver = "0.4.8"
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
    "exo-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libkeybinder3-devel",
    "libnotify-devel",
    "libpulse-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
    # "libxfce4windowing-devel" when xfce 4.20
]
# Default mixer
depends = ["pavucontrol"]
pkgdesc = "Xfce pulseaudio panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-pulseaudio-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-pulseaudio-plugin/{pkgver[:-2]}/xfce4-pulseaudio-plugin-{pkgver}.tar.bz2"
sha256 = "bd742b207c39c221e91c57c9c9be2839eb802d1b1ee01a02b7427cd02d3f0348"
