pkgname = "libxkbui"
pkgver = "1.0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxt-devel", "libxkbfile-devel"]
pkgdesc = "X.org libxkbui library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.bz2"
sha256 = "20c23101d63234ee5f6d696dfa069b29c6c58e39eff433bcd7705b50b3ffa214"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxkbui-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
