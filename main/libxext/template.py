pkgname = "libxext"
pkgver = "1.3.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXext-{pkgver}.tar.xz"
sha256 = "edb59fa23994e405fdc5b400afdf5820ae6160b94f35e3dc3da4457a16e89753"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxext-devel")
def _devel(self):
    return self.default_devel()
