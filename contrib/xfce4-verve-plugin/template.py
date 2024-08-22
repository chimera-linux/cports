pkgname = "xfce4-verve-plugin"
pkgver = "2.0.3"
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
    "pcre2-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce command line panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-verve-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-verve-plugin/{pkgver[:-2]}/xfce4-verve-plugin-{pkgver}.tar.bz2"
sha256 = "e1bf121f1bf9cf2a199bf5c0f3aa802f503df9bea50724741e7a92fe6d9fe09e"
