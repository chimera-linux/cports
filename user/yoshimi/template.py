pkgname = "yoshimi"
pkgver = "2.3.3.3"
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
sha256 = "10b70d6bf577de3f36883b0e066d5de0b7291d4e4de3dee3b56df68feaed9469"
