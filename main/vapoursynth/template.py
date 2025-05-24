pkgname = "vapoursynth"
pkgver = "71"
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
sha256 = "c56d6de16d0a24db7eee1bd5e633229b0bd8a746eafcfe41945a22f9d44f8bd6"


@subpackage("vapoursynth-devel")
def _(self):
    return self.default_devel()
