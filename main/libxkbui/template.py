pkgname = "libxkbui"
pkgver = "1.0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxt-devel", "libxkbfile-devel"]
pkgdesc = "X.org libxkbui library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libxkbui-{pkgver}.tar.bz2"
sha256 = "20c23101d63234ee5f6d696dfa069b29c6c58e39eff433bcd7705b50b3ffa214"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxkbui-devel")
def _(self):
    return self.default_devel()
