pkgname = "xvidcore"
pkgver = "1.3.7"
pkgrel = 1
build_wrksrc = "build/generic"
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake", "libtool", "nasm"]
pkgdesc = "ISO MPEG-4 compliant video codec"
license = "GPL-2.0-or-later"
url = "https://www.xvid.com"
source = f"https://downloads.xvid.com/downloads/xvidcore-{pkgver}.tar.bz2"
sha256 = "aeeaae952d4db395249839a3bd03841d6844843f5a4f84c271ff88f7aa1acff7"
# no check target
options = ["!check"]


@subpackage("xvidcore-devel")
def _(self):
    return self.default_devel()
