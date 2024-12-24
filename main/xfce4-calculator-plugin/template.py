pkgname = "xfce4-calculator-plugin"
pkgver = "0.7.3"
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
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce calculator panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-calculator-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-calculator-plugin/{pkgver[:-2]}/xfce4-calculator-plugin-{pkgver}.tar.bz2"
sha256 = "3feb5f56092ceef2858c3c1bd443317d4caf289a6409f9db506f49088e19a2e8"
