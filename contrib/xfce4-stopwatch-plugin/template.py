pkgname = "xfce4-stopwatch-plugin"
pkgver = "0.5.0"
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
    "libwnck-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce stopwatch panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://docs.xfce.org/panel-plugins/xfce4-stopwatch-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-stopwatch-plugin/{pkgver[:-2]}/xfce4-stopwatch-plugin-{pkgver}.tar.bz2"
sha256 = "7c1b5e3401874daa0bc6c9ecfdd85f16b6dfc5c089709a18a4b87d89920004e1"


def post_install(self):
    self.install_license("COPYING")
