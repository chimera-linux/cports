pkgname = "libbs2b"
pkgver = "3.1.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["libsndfile-devel"]
pkgdesc = "Bauer stereophonic-to-binaural DSP"
license = "MIT"
url = "http://bs2b.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/bs2b/libbs2b/{pkgver}/libbs2b-{pkgver}.tar.gz"
sha256 = "6aaafd81aae3898ee40148dd1349aab348db9bfae9767d0e66e0b07ddd4b2528"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libbs2b-devel")
def _(self):
    return self.default_devel()
