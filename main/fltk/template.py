pkgname = "fltk"
pkgver = "1.3.9"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.0-only WITH FLTK-exception"
url = "https://www.fltk.org"
source = f"{url}/pub/fltk/{pkgver}/fltk-{pkgver}-source.tar.gz"
sha256 = "d736b0445c50d607432c03d5ba5e82f3fba2660b10bc1618db8e077a42d9511b"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("fltk-devel")
def _(self):
    return self.default_devel(extra=["usr/share/fltk"])
