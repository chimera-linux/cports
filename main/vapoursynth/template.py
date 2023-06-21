pkgname = "vapoursynth"
pkgver = "63"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "automake",
    "libtool",
    "nasm",
    "python-cython",
]
makedepends = ["python-devel", "zimg-devel"]
pkgdesc = "Video processing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.vapoursynth.com"
source = f"https://github.com/vapoursynth/vapoursynth/archive/R{pkgver}.tar.gz"
sha256 = "ed909b3c58e79bcbb056d07c5d301222ba8001222b4b40d5c1123be35fea9ae2"

tool_flags = {"CFLAGS": [], "CXXFLAGS": [], "LDFLAGS": []}

if self.profile().arch == "riscv64":
    # ld: error: section size decrease too large
    tool_flags["CFLAGS"] += ["-mno-relax"]
    tool_flags["CXXFLAGS"] += ["-mno-relax"]
    tool_flags["LDFLAGS"] += ["-mno-relax"]


@subpackage("vapoursynth-devel")
def _devel(self):
    # libvapoursynth.so should be in main package, don't use default_devel
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.a",
        "usr/lib/libvapoursynth-script.so",
    ]
