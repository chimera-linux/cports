pkgname = "padthv1"
pkgver = "1.1.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "fftw-devel",
    "liblo-devel",
    "libsndfile-devel",
    "lv2",
    "pipewire-jack-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "Polyphonic additive synthesizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://padthv1.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/padthv1/padthv1-{pkgver}.tar.gz"
sha256 = "55bbfbe9f28082e5eaf32c722ec6321de3b4784e25801c2606018dcd4b41de12"
