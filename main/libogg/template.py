pkgname = "libogg"
pkgver = "1.3.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
pkgdesc = "Ogg bitstream file format library"
license = "BSD-3-Clause"
url = "https://www.xiph.org/ogg"
source = f"https://downloads.xiph.org/releases/ogg/libogg-{pkgver}.tar.xz"
sha256 = "5c8253428e181840cd20d41f3ca16557a9cc04bad4a3d04cce84808677fa1061"
# FIXME int
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libogg-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])
