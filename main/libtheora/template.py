pkgname = "libtheora"
pkgver = "1.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-examples",
    "--disable-vorbistest",
    "--disable-sdltest",
]
# fails to regen
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libogg-devel"]
pkgdesc = "Theora video compression codec"
license = "BSD-3-Clause"
url = "https://theora.org"
source = f"https://downloads.xiph.org/releases/theora/libtheora-{pkgver}.tar.xz"
sha256 = "ebdf77a8f5c0a8f7a9e42323844fa09502b34eb1d1fece7b5f54da41fe2122ec"
# FIXME int
hardening = ["!int"]
# lto miscompiles in analyze.c
options = ["!lto"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libtheora-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])
