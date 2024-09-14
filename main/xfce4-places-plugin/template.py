pkgname = "xfce4-places-plugin"
pkgver = "1.8.3"
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
    "libnotify-devel",
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce folders and media quick access panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-places-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-places-plugin/{pkgver[:-2]}/xfce4-places-plugin-{pkgver}.tar.bz2"
sha256 = "f11d0e6d03f22ab02c2e6b507d365b5a918532e8819e50647ee1860eca60c743"
