pkgname = "gparted"
pkgver = "1.8.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-libparted-dmraid",
]
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
license = "GPL-2.0-or-later"
url = "https://gparted.org"
source = f"$(SOURCEFORGE_SITE)/gparted/gparted-{pkgver}.tar.gz"
sha256 = "67388ac405f9fe92a40636cb03b0e1e0bb6403ad89ccc174b2ff190ef6f32349"
# needs /dev setup from udev
options = ["!check"]
