pkgname = "xkill"
pkgver = "1.0.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "Kill an X client by its X resource"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xkill-{pkgver}.tar.gz"
sha256 = "aec5674d48d1749742e87dfbff30f1abacabe5e2a10c0679c3996882444c9f6d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
