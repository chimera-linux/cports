pkgname = "fltk"
pkgver = "1.4.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
    "-DFLTK_BUILD_SHARED_LIBS=ON",
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
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "glu-devel",
    "libdecor-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxext-devel",
    "libxft-devel",
    "libxkbcommon-devel",
    "libxinerama-devel",
    "mesa-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Cross-platform C++ GUI toolkit"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.0-only WITH FLTK-exception"
url = "https://www.fltk.org"
source = f"https://github.com/fltk/fltk/releases/download/release-{pkgver}/fltk-{pkgver}-source.tar.gz"
sha256 = "7d0a5a352fde0beae44a2009c1aca1d6be15d46dd251d1c12cf34d752b429038"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("fltk-devel")
def _(self):
    self.depends += ["pango-devel"]
    return self.default_devel(extra=["usr/share/fltk"])
