pkgname = "xwud"
pkgver = "1.0.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel"]
pkgdesc = "X image displayer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xwud-{pkgver}.tar.xz"
sha256 = "e55cbedab36d7a5f671abf8e594888afc48caa116d51d429ea53ea317ec0c61e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
