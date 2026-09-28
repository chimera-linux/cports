pkgname = "libxkbfile"
pkgver = "1.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "Xkbfile library from X.org"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libxkbfile-{pkgver}.tar.xz"
sha256 = "7f71884e5faf56fb0e823f3848599cf9b5a9afce51c90982baeb64f635233ebf"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxkbfile-devel")
def _(self):
    return self.default_devel()
