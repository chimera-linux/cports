pkgname = "xfce4-smartbookmark-plugin"
pkgver = "0.6.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce browser search panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-smartbookmark-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-smartbookmark-plugin/{pkgver[:-2]}/xfce4-smartbookmark-plugin-{pkgver}.tar.xz"
sha256 = "d8a619dcad703071f7fcda538cc34154f9952cf4ec0816df23a56e98e3cc05d8"
