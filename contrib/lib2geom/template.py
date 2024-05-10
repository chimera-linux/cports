pkgname = "lib2geom"
pkgver = "1.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-D2GEOM_BUILD_SHARED=ON",
    "-D2GEOM_TESTING=ON",
]
make_check_args = [
    "-E",
    "("
    # tiny floating point errors
    + "circle-test|ellipse-test"
    # ??
    + "|bezier-test|elliptical-arc-test)",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python-cython",
    "ragel",
]
makedepends = [
    "boost-devel",
    "cairo-devel",
    "double-conversion-devel",
    "gsl-devel",
    "gtest-devel",
    "gtk+3-devel",
]
pkgdesc = "2D geometry library for C++"
maintainer = "psykose <alice@ayaya.dev>"
license = "MPL-1.1 OR LGPL-2.1-only"
url = "https://gitlab.com/inkscape/lib2geom"
source = f"https://gitlab.com/inkscape/lib2geom/-/archive/{pkgver}/lib2geom-{pkgver}.tar.gz"
sha256 = "732a81c6564d5c388bae44f0fdd350f628375e23294941abbe928ab87ec937ab"


@subpackage("lib2geom-devel")
def _devel(self):
    return self.default_devel()
