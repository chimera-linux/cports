pkgname = "xfce4-windowck-plugin"
pkgver = "0.5.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
    "python",
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
pkgdesc = "Xfce window controls/title bar panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-windowck-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-windowck-plugin/{pkgver[:-2]}/xfce4-windowck-plugin-{pkgver}.tar.bz2"
sha256 = "a781448b781e984d3bda59b0daab0d184d4cec2252316f7370ac4a98efe481f4"
