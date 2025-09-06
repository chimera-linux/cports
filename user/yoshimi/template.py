pkgname = "yoshimi"
pkgver = "2.3.4.1"
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
license = "GPL-2.0-or-later"
url = "https://yoshimi.github.io"
source = f"https://github.com/Yoshimi/yoshimi/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2ab49688c42038863a6e5807055d0911ac069ca1527afbbbb93eb50595820d40"
# FIXME lintpixmaps
options = ["!lintpixmaps"]
