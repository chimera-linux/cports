pkgname = "libxpm"
pkgver = "3.5.15"
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
sha256 = "2a9bd419e31270593e59e744136ee2375ae817322447928d2abb6225560776f9"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxpm-devel")
def _devel(self):
    return self.default_devel()
