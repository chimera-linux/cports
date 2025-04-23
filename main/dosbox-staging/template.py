pkgname = "dosbox-staging"
pkgver = "0.82.1"
pkgrel = 0
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
sha256 = "9d943d6610b6773cb0b27ba24904c85459757fbbfa0f34c72e76082132f77568"
# CFI: breaks the tests
hardening = ["!cfi", "vis"]
