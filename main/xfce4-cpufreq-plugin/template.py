pkgname = "xfce4-cpufreq-plugin"
pkgver = "1.2.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce CPU governor and frequency panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-cpufreq-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-cpufreq-plugin/{pkgver[:-2]}/xfce4-cpufreq-plugin-{pkgver}.tar.bz2"
sha256 = "d0714720d588c649457590e5de3d95859b922a98d5fa9d0d1416f36a76bd3ef9"
