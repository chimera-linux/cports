pkgname = "yoshimi"
pkgver = "2.3.3"
pkgrel = 0
build_style = "cmake"
cmake_dir = "src"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "argp-standalone",
    "cairo-devel",
    "fftw-devel",
    "fltk-devel",
    "fontconfig-devel",
    "libedit-readline-devel",
    "lv2",
    "mesa-devel",
    "mxml3-devel",
    "pipewire-jack-devel",
]
pkgdesc = "Software synthesizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://yoshimi.github.io"
source = f"https://github.com/Yoshimi/yoshimi/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f15ff1a909c273ea75febfd15655560a556b6b832afe57f918ea966702daf2f6"
