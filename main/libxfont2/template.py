pkgname = "libxfont2"
pkgver = "2.0.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = [
    "freetype-devel",
    "libfontenc-devel",
    "xorgproto",
    "xtrans",
]
pkgdesc = "X font 2 library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXfont2-{pkgver}.tar.xz"
sha256 = "f556c0e1093a4e6911cc90bc4b106d201902ee187fd74af206ff162f7e6a24d5"
# FIXME int (e.g. xorg fails check)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxfont2-devel")
def _(self):
    return self.default_devel()
