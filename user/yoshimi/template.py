pkgname = "yoshimi"
pkgver = "2.3.5.1"
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
sha256 = "f9676ee9a37a21e736f3a215dfd8098b428a156d74f681c354505b5e3e9a3bdc"
# FIXME lintpixmaps
options = ["!lintpixmaps"]
