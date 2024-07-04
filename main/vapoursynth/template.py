pkgname = "vapoursynth"
pkgver = "69"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
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
sha256 = "cbd5421df85ba58228ea373cc452ca677e0e2ec61b59944d7e514234633057d9"


@subpackage("vapoursynth-devel")
def _devel(self):
    return self.default_devel()
