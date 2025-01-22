pkgname = "smpeg"
pkgver = "2.0.0"
pkgrel = 2
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["sdl2-compat-devel"]
pkgdesc = "MPEG decoding library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://icculus.org/smpeg"
source = f"https://www.libsdl.org/projects/smpeg/release/smpeg2-{pkgver}.tar.gz"
sha256 = "979a65b211744a44fa641a9b6e4d64e64a12ff703ae776bafe3c4c4cd85494b3"
tool_flags = {"CFLAGS": ["-Wno-register"]}
# no check target
options = ["!check"]


def post_extract(self):
    # breaks smpeg-config because it bad
    self.rm("acinclude/sdl2.m4")


@subpackage("smpeg-devel")
def _(self):
    return self.default_devel()
