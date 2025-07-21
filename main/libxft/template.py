pkgname = "libxft"
pkgver = "2.3.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "libxrender-devel",
    "xorgproto",
]
pkgdesc = "X font library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXft-{pkgver}.tar.gz"
sha256 = "47c157fb4d0308f8b9604b74c29bb902b019eb97031f8fbf5ab62aa9f147a104"
# crashes
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxft-devel")
def _(self):
    return self.default_devel()
