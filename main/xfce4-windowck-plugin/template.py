pkgname = "xfce4-windowck-plugin"
pkgver = "0.5.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "python",
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
    "xfconf-devel",
]
pkgdesc = "Xfce window controls/title bar panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-windowck-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-windowck-plugin/{pkgver[:-2]}/xfce4-windowck-plugin-{pkgver}.tar.bz2"
sha256 = "dc4ed5dc94bd05de5495441f0cabb260ab3e1f6ce27b1fac92e37f909c0cfe0a"
