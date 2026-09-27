pkgname = "qalculate-gtk"
# match to libqalculate
pkgver = "5.12.0"
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
sha256 = "4225eacefc30354f867dc14b7974efe8e8fcef031117def1098db652e1ad48b7"
