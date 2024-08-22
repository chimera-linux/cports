pkgname = "xfce4-notes-plugin"
pkgver = "1.11.0"
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
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce notes panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-notes-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-notes-plugin/{pkgver[:-2]}/xfce4-notes-plugin-{pkgver}.tar.bz2"
sha256 = "eb38246deb0fc89535fa9ff9b953c762cece232b5585d8210fab9abbf282aae3"
