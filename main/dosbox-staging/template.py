pkgname = "dosbox-staging"
pkgver = "0.82.2"
pkgrel = 2
build_style = "meson"
configure_args = ["-Duse_zlib_ng=false"]
hostmakedepends = ["bash", "meson", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "fluidsynth-devel",
    "gtest-devel",
    "iir1-devel",
    "libpng-devel",
    "libslirp-devel",
    "mt32emu-devel",
    "opusfile-devel",
    "sdl2-compat-devel",
    "sdl2_net-devel",
    "speexdsp-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Modern continuation of DOSBox"
license = "GPL-2.0-or-later"
url = "https://www.dosbox-staging.org"
source = f"https://github.com/dosbox-staging/dosbox-staging/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "387c97b373c3164ab5abbbc2b210bf94b5567057abe44ee1e8b4d4e725bd422c"
# CFI: breaks the tests
hardening = ["!cfi", "vis"]
