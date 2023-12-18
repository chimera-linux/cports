pkgname = "vapoursynth"
pkgver = "65"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
make_dir = "."
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
sha256 = "2bde5233b82d914b5e985119ed9cc344e3c27c3c068b5c4ab909176cd1751dce"


@subpackage("vapoursynth-devel")
def _devel(self):
    # libvapoursynth.so should be in main package, don't use default_devel
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.a",
        "usr/lib/libvapoursynth-script.so",
    ]
