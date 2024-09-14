pkgname = "xfce4-eyes-plugin"
pkgver = "4.6.0"
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
    "gtk+3-devel",
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce eyes panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-eyes-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-eyes-plugin/{pkgver[:-2]}/xfce4-eyes-plugin-{pkgver}.tar.bz2"
sha256 = "ad0ff05d88ba393b7c8922f8233edd33fc0a4e8b000b61de1f8f3a10c5ae5324"
