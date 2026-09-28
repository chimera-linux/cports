pkgname = "xfce4-dict"
pkgver = "0.8.9"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce dictionary search app"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-dict/start"
source = (
    f"$(XFCE_SITE)/apps/xfce4-dict/{pkgver[:-2]}/xfce4-dict-{pkgver}.tar.xz"
)
sha256 = "f1a81baad1e60496aeffc8f8ef1be6413c732b09e250d52d062d293ade001a8c"
