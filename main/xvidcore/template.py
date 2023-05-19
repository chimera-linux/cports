pkgname = "xvidcore"
pkgver = "1.3.7"
pkgrel = 0
build_wrksrc = "build/generic"
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "nasm"]
pkgdesc = "ISO MPEG-4 compliant video codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.xvid.com"
source = f"https://downloads.xvid.com/downloads/{pkgname}-{pkgver}.tar.bz2"
sha256 = "aeeaae952d4db395249839a3bd03841d6844843f5a4f84c271ff88f7aa1acff7"
# FIXME check
hardening = ["!int"]
# no check target
options = ["!check"]

@subpackage("xvidcore-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
