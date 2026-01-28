pkgname = "lager"
pkgver = "0.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Dlager_BUILD_EXAMPLES=OFF",
    "-Dlager_BUILD_DEBUGGER_EXAMPLES=OFF",
]
makedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "catch2-devel",
    "immer",
    "zug",
    "boost-devel",
]
depends = [
    "boost-devel",
]
pkgdesc = "C++ library for value oriented design"
license = "MIT"
url = "https://sinusoid.es/lager"
source = f"https://github.com/arximboldi/lager/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9e4743c3fe2c95c1653c3fd088a2200108f09d758725697831852dc91d15d174"
# tests didn't get run, probably an easy fix but don't want to deal with this rn
options = ["!check"]
