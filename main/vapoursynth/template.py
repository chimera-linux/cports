pkgname = "vapoursynth"
pkgver = "73"
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
license = "LGPL-2.1-or-later"
url = "https://www.vapoursynth.com"
source = f"https://github.com/vapoursynth/vapoursynth/archive/R{pkgver}.tar.gz"
sha256 = "1bb8ffe31348eaf46d8f541b138f0136d10edaef0c130c1e5a13aa4a4b057280"


@subpackage("vapoursynth-devel")
def _(self):
    return self.default_devel()
