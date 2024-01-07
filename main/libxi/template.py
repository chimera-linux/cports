pkgname = "libxi"
pkgver = "1.8.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = [
    "pkgconf",
    "xmlto",
    "automake",
    "libtool",
    "xorg-util-macros",
]
makedepends = ["xorgproto", "libxfixes-devel", "libxext-devel"]
pkgdesc = "X Input extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXi-{pkgver}.tar.gz"
sha256 = "3b5f47c223e4b63d7f7fe758886b8bf665b20a7edb6962c423892fd150e326ea"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxi-devel")
def _devel(self):
    return self.default_devel()
