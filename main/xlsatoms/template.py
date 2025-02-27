pkgname = "xlsatoms"
pkgver = "1.1.4"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libxcb-devel"]
pkgdesc = "List interned atoms defined on the X server"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xlsatoms-{pkgver}.tar.gz"
sha256 = "e3b4dce0e6bf3b60bc308ed184d2dc201ea4af6ce03f0126aa303ccd1ccb1237"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
