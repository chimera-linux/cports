pkgname = "libxpm"
pkgver = "3.5.16"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-open-zfile"]
hostmakedepends = ["pkgconf", "gettext-tiny"]
makedepends = ["xorgproto", "libsm-devel", "libxext-devel", "libxt-devel"]
pkgdesc = "X PixMap library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXpm-{pkgver}.tar.gz"
sha256 = "43a70e6f9b67215fb223ca270d83bdcb868c513948441d5b781ea0765df6bfb4"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxpm-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
