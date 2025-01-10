pkgname = "xfce4-stopwatch-plugin"
pkgver = "0.5.2"
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
sha256 = "b5a458fa5b7538d42cd9783cf4c26eafe0c9d394906a0e5e25bb3fe0adc34c08"


def post_install(self):
    self.install_license("COPYING")
