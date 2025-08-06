pkgname = "qalculate-gtk"
# match to libqalculate
pkgver = "5.7.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "libqalculate-devel",
    "libxml2-devel",
]
pkgdesc = "GTK+3 frontend for libqalculate"
license = "GPL-2.0-or-later"
url = "https://qalculate.github.io"
source = f"https://github.com/Qalculate/qalculate-gtk/releases/download/v{pkgver}/qalculate-gtk-{pkgver}.tar.gz"
sha256 = "dcb3663b36abafdfe32e943644bf4fc64bd685c0225f944a3f1c4a85e70db3b5"
