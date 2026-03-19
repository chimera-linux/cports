pkgname = "qalculate-gtk"
# match to libqalculate
pkgver = "5.9.0"
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
sha256 = "39cd0bc5abe26edfc04a3064d4412d5af9f7197eafa0762a18a0cb6996f1021b"
