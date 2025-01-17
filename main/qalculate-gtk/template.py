pkgname = "qalculate-gtk"
# match to libqalculate
pkgver = "5.5.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://qalculate.github.io"
source = f"https://github.com/Qalculate/qalculate-gtk/releases/download/v{pkgver}/qalculate-gtk-{pkgver}.tar.gz"
sha256 = "89840c16deba524b23512dc6d8d91f74f282c672a2ad001533f4b063d49171dd"
