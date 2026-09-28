pkgname = "xfce4-netload-plugin"
pkgver = "1.5.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libxfce4ui-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce network load panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-netload-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-netload-plugin/{pkgver[:-2]}/xfce4-netload-plugin-{pkgver}.tar.xz"
sha256 = "a868be8f73e8396c2d61903d46646993c5130d16ded71ddb5da9088abf7cb7ba"
