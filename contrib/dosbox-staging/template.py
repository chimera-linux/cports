pkgname = "dosbox-staging"
pkgver = "0.81.1"
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
    "zlib-devel",
]
pkgdesc = "Modern continuation of DOSBox"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://www.dosbox-staging.org"
source = f"https://github.com/dosbox-staging/dosbox-staging/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2b389fdc338454f916240aab5a2ae5560d1dd9808d63c70f34ec9a91e60b535a"
# FIXME: cfi breaks the tests
hardening = ["!cfi", "vis"]
