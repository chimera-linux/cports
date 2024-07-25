pkgname = "dosbox-staging"
pkgver = "0.81.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Duse_zlib_ng=false"]
hostmakedepends = ["meson", "pkgconf"]
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
sha256 = "6676a3b6957c144a80ca8c3ffec2a0bec0320274382f23af9c57dd1c20b2eb1b"
# CFI: breaks the tests
hardening = ["!cfi", "vis"]
