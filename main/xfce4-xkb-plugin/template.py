pkgname = "xfce4-xkb-plugin"
pkgver = "0.8.3"
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
    "garcon-devel",
    "gtk+3-devel",
    "libnotify-devel",
    "librsvg-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxklavier-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce keyboard layout panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-xkb-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-xkb-plugin/{pkgver[:-2]}/xfce4-xkb-plugin-{pkgver}.tar.bz2"
sha256 = "f0bfe97875ef1ca0a3b6a6fac312663c9cada151cf1ac96071393d320cd04987"
