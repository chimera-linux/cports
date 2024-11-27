pkgname = "fltk"
pkgver = "1.3.10"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
    # not actual tests, just test programs
    "-DFLTK_BUILD_TEST=ON",
    "-DOPTION_CAIRO=ON",
    "-DOPTION_CAIROEXT=ON",
    "-DOPTION_BUILD_SHARED_LIBS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libx11-devel",
    "libxext-devel",
    "libxft-devel",
    "libxinerama-devel",
    "mesa-devel",
]
pkgdesc = "Cross-platform C++ GUI toolkit"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.0-only WITH FLTK-exception"
url = "https://www.fltk.org"
source = f"{url}/pub/fltk/{pkgver}/fltk-{pkgver}-source.tar.gz"
sha256 = "c1c96d4f2ca7844f4b7945b4670aff2846f150cd5f3e23e3e4c70a61807108c7"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("fltk-devel")
def _(self):
    return self.default_devel(extra=["usr/share/fltk"])
