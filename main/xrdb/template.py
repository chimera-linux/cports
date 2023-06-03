pkgname = "xrdb"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-cpp=/usr/bin/clang-cpp,/usr/bin/cpp"]
hostmakedepends = ["pkgconf", "automake", "libtool", "xorg-util-macros"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "X server resource database utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "db2d774a35ae2f7e7ac61cc2de0dcae27fc2aa14399c35721f8300e63ea73549"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
