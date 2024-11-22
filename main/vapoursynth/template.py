pkgname = "vapoursynth"
pkgver = "70.11"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "nasm",
    "pkgconf",
    "python-cython",
]
makedepends = ["python-devel", "zimg-devel"]
pkgdesc = "Video processing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.vapoursynth.com"
source = f"https://github.com/vapoursynth/vapoursynth/archive/R{pkgver}.tar.gz"
sha256 = "41af974964a20aec670f5d2b235e043cb9c3a68db90fa39cc57c609c7d8baa91"


@subpackage("vapoursynth-devel")
def _(self):
    return self.default_devel()
