pkgname = "vapoursynth"
pkgver = "61"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "automake", "libtool", "nasm", "python-cython"
]
makedepends = ["python-devel", "zimg-devel"]
pkgdesc = "Video processing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.vapoursynth.com"
source = f"https://github.com/vapoursynth/vapoursynth/archive/R{pkgver}.tar.gz"
sha256 = "a5d4feeb056679dd1204153250d7c1d38e5a639e995d3c4e3a8e2e8fe1425b75"

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

@subpackage("vapoursynth-devel")
def _devel(self):
    # libvapoursynth.so should be in main package, don't use default_devel
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.a",
        "usr/lib/libvapoursynth-script.so",
    ]
