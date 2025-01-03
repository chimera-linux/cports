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
sha256 = "a3f63f86bf203ba28512e189ce6736cdb0273647e77a62ce47ed3d01b3b4a88d"
# CFI: breaks the tests
hardening = ["!cfi", "vis"]
