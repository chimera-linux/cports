pkgname = "qalculate-gtk"
# match to libqalculate
pkgver = "5.5.1"
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
sha256 = "dcf33e89ec2539c3e0bf9c5aee18b44680f6630b1e02cf23e2e9add6578450c7"
