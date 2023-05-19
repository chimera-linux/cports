pkgname = "vapoursynth"
pkgver = "62"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
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
sha256 = "6f3eb7e2e32a0572b363e08d16092418e99bd9c8f06661645a0995f1f736d438"

if self.profile().arch == "riscv64":
    # ld: error: section size decrease too large
    tool_flags = {
        "CFLAGS": ["-mno-relax"],
        "CXXFLAGS": ["-mno-relax"],
        "LDFLAGS": ["-mno-relax"]
    }

@subpackage("vapoursynth-devel")
def _devel(self):
    # libvapoursynth.so should be in main package, don't use default_devel
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.a",
        "usr/lib/libvapoursynth-script.so",
    ]
