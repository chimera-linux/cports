pkgname = "xfce4-cpugraph-plugin"
pkgver = "1.2.11"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce clipboard manager app and panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-cpugraph-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-cpugraph-plugin/{pkgver[: pkgver.rfind('.')]}/xfce4-cpugraph-plugin-{pkgver}.tar.bz2"
sha256 = "58aa31df1934afc2a352744754a730a3d796b1246e12c7a5e86f7b6a403ca20d"


def post_install(self):
    # TODO: figure out why build system installs this
    self.uninstall("usr/lib/xfce4/panel/plugins/libcpugraph.a")
