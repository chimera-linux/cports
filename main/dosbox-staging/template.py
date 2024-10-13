pkgname = "dosbox-staging"
pkgver = "0.82.0"
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
    "sdl-devel",
    "sdl_net-devel",
    "speexdsp-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Modern continuation of DOSBox"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.dosbox-staging.org"
source = f"https://github.com/dosbox-staging/dosbox-staging/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "96556debe87f4b4a1397293be5c3311de9d736cc5d51e8b0ab4ffe93bc42cfbf"
# CFI: breaks the tests
hardening = ["!cfi", "vis"]
