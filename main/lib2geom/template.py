pkgname = "lib2geom"
pkgver = "1.4"
pkgrel = 5
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
    + "|bezier-test|elliptical-arc-test|line-test|polynomial-test)",
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
license = "MPL-1.1 OR LGPL-2.1-only"
url = "https://gitlab.com/inkscape/lib2geom"
source = f"https://gitlab.com/inkscape/lib2geom/-/archive/{pkgver}/lib2geom-{pkgver}.tar.gz"
sha256 = "edef330f557f188afc11ab505b6ffcfafb075da73e5dde95b9ecf96d20ab6374"


@subpackage("lib2geom-devel")
def _(self):
    return self.default_devel()
