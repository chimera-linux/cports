pkgname = "fltk"
pkgver = "1.4.4"
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
    "libxinerama-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Cross-platform C++ GUI toolkit"
license = "LGPL-2.0-only WITH FLTK-exception"
url = "https://www.fltk.org"
source = f"https://github.com/fltk/fltk/releases/download/release-{pkgver}/fltk-{pkgver}-source.tar.gz"
sha256 = "94b464cce634182c8407adac1be5fc49678986ca93285699b444352af89b4efe"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("fltk-devel")
def _(self):
    self.depends += ["pango-devel"]
    return self.default_devel(extra=["usr/share/fltk"])
