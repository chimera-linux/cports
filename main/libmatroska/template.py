pkgname = "libmatroska"
pkgver = "1.7.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["libebml-devel"]
pkgdesc = "C++ libary to parse Matroska files"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/Matroska-Org/libmatroska"
source = (
    f"https://dl.matroska.org/downloads/libmatroska/libmatroska-{pkgver}.tar.xz"
)
sha256 = "572a3033b8d93d48a6a858e514abce4b2f7a946fe1f02cbfeca39bfd703018b3"


@subpackage("libmatroska-devel")
def _(self):
    return self.default_devel()
