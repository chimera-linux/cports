pkgname = "libtheora"
pkgver = "1.1.1"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://theora.org"
source = f"https://downloads.xiph.org/releases/theora/libtheora-{pkgver}.tar.xz"
sha256 = "f36da409947aa2b3dcc6af0a8c2e3144bc19db2ed547d64e9171c59c66561c61"
# FIXME int
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libtheora-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])
