pkgname = "speexdsp"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf",
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Speex DSP library"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://www.speex.org"
source = f"https://gitlab.xiph.org/xiph/speexdsp/-/archive/SpeexDSP-{pkgver}/speexdsp-SpeexDSP-{pkgver}.tar.bz2"
sha256 = "b36d4f16e42b7103b7fc3e4a8f98b6bf889dd1f70f65c2365af07be82844db29"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("speexdsp-devel")
def _devel(self):
    return self.default_devel()
