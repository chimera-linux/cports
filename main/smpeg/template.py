pkgname = "smpeg"
pkgver = "2.0.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["sdl-devel"]
pkgdesc = "MPEG decoding library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://icculus.org/smpeg"
source = f"https://www.libsdl.org/projects/smpeg/release/smpeg2-{pkgver}.tar.gz"
sha256 = "979a65b211744a44fa641a9b6e4d64e64a12ff703ae776bafe3c4c4cd85494b3"
# no check target
options = ["!check"]


@subpackage("smpeg-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
