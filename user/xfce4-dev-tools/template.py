pkgname = "xfce4-dev-tools"
pkgver = "4.20.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "slibtool",
]
makedepends = ["glib-devel"]
pkgdesc = "Xfce development tools"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfce4-dev-tools/start"
source = f"$(XFCE_SITE)/xfce/xfce4-dev-tools/{pkgver[:-2]}/xfce4-dev-tools-{pkgver}.tar.bz2"
sha256 = "1fba39a08a0ecc771eaa3a3b6e4272a4f0b9e7c67d0f66e780cd6090cd4466aa"
