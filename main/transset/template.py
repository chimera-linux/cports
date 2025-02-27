pkgname = "transset"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libxt-devel"]
pkgdesc = "Sets the transparency of an X window"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/transset-{pkgver}.tar.gz"
sha256 = "57435a2619a40db912f6e5660f785963e94c57f1874819f647210be598d280c3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
