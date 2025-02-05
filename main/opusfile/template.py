pkgname = "opusfile"
pkgver = "0.12"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libogg-devel", "opus-devel", "openssl3-devel"]
pkgdesc = "Library for opening, seeking, and decoding .opus files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.opus-codec.org"
source = f"http://downloads.xiph.org/releases/opus/opusfile-{pkgver}.tar.gz"
sha256 = "118d8601c12dd6a44f52423e68ca9083cc9f2bfe72da7a8c1acb22a80ae3550b"
# CFI: crashes in deadbeef when loading a .ogg
hardening = ["vis", "!cfi"]


def post_install(self):
    self.uninstall("usr/share")
    self.install_license("COPYING")


@subpackage("opusfile-devel")
def _(self):
    return self.default_devel()
