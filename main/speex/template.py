pkgname = "speex"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["fftw-devel", "libogg-devel", "speexdsp-devel"]
pkgdesc = "Free audio codec for speech"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.speex.org"
source = f"https://downloads.xiph.org/releases/speex/speex-{pkgver}.tar.gz"
sha256 = "4b44d4f2b38a370a2d98a78329fefc56a0cf93d1c1be70029217baae6628feea"
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("speex-devel")
def _(self):
    return self.default_devel()
