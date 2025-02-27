pkgname = "libxfont2"
pkgver = "2.0.7"
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
sha256 = "8b7b82fdeba48769b69433e8e3fbb984a5f6bf368b0d5f47abeec49de3e58efb"
# FIXME int (e.g. xorg fails check)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxfont2-devel")
def _(self):
    return self.default_devel()
