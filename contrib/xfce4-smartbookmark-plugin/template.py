pkgname = "xfce4-smartbookmark-plugin"
pkgver = "0.5.2"
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
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce browser search panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-smartbookmark-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-smartbookmark-plugin/{pkgver[:-2]}/xfce4-smartbookmark-plugin-{pkgver}.tar.bz2"
sha256 = "2a279e2f5a54518684e62ad1f3cd8ef950826505b39725f1b5d8f0c43031cdd3"
