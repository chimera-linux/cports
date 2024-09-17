pkgname = "vapoursynth"
pkgver = "70"
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
sha256 = "59c813ec36046be33812408ff00e16cae63c6843af6acf4e34595910a80e267b"


@subpackage("vapoursynth-devel")
def _(self):
    return self.default_devel()
