pkgname = "gparted"
pkgver = "1.6.0"
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
    "libuuid-devel",
    "parted-devel",
    "polkit-devel",
]
pkgdesc = "Graphical disk partition editor"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gparted.org"
source = f"$(SOURCEFORGE_SITE)/gparted/gparted-{pkgver}.tar.gz"
sha256 = "9b9f51b3ce494ddcb59a55e1ae6679c09436604e331dbf5a536d60ded6c6ea5b"
# needs /dev setup from udev
options = ["!check"]
