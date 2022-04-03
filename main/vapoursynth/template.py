pkgname = "vapoursynth"
pkgver = "57"
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
sha256 = "9bed2ab1823050cfcbdbb1a57414e39507fd6c73f07ee4b5986fcbf0f6cb2d07"

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
