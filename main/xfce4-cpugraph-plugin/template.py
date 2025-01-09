pkgname = "xfce4-cpugraph-plugin"
pkgver = "1.2.10"
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
pkgdesc = "Xfce clipboard manager app and panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-cpugraph-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-cpugraph-plugin/{pkgver[: pkgver.rfind('.')]}/xfce4-cpugraph-plugin-{pkgver}.tar.bz2"
sha256 = "37792dd052691712195658169b95fb6583f924485ce7a467b33d01e08775d915"
