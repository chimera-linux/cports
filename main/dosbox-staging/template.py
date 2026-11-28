pkgname = "dosbox-staging"
pkgver = "0.83.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUSE_SYSTEM_LIBS=ON", "-DRESOURCE_COPY_PATH=resources/"]
make_check_args = ["-j1"]
hostmakedepends = ["bash", "cmake", "fluidsynth", "ninja", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "asio",
    "fluidsynth-devel",
    "gtest-devel",
    "iir1-devel",
    "libpng-devel",
    "libslirp-devel",
    "mt32emu-devel",
    "opusfile-devel",
    "sdl2-compat-devel",
    "sdl2_image-devel",
    "speexdsp-devel",
    "zlib-ng-devel",
]
pkgdesc = "Modern continuation of DOSBox"
license = "GPL-2.0-or-later"
url = "https://www.dosbox-staging.org"
source = f"https://github.com/dosbox-staging/dosbox-staging/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "14c3703369e56125a425aea8ebb1a425823df58f9769f3e48b1b8ebbf2c6cf09"
# CFI: breaks the tests
# int: natural_compare function can oveflow integer
hardening = ["!cfi", "!int", "vis"]
