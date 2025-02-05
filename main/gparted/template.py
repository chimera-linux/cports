pkgname = "gparted"
pkgver = "1.7.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-libparted-dmraid"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "itstool",
    "libtool",
    "libxml2-progs",
    "pkgconf",
    "yelp-tools",
]
makedepends = [
    "gtkmm3.0-devel",
    "parted-devel",
    "polkit-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "Graphical disk partition editor"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gparted.org"
source = f"$(SOURCEFORGE_SITE)/gparted/gparted-{pkgver}.tar.gz"
sha256 = "84ae3b9973e443a2175f07aa0dc2aceeadb1501e0f8953cec83b0ec3347b7d52"
# needs /dev setup from udev
options = ["!check"]
