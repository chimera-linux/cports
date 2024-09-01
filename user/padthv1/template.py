pkgname = "padthv1"
pkgver = "1.1.0"
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
pkgdesc = "Polythonic additive synthesizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://padthv1.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/padthv1/padthv1-{pkgver}.tar.gz"
sha256 = "a81f8f9bb8d2193f4df08b76eef7c6a08fae16ee2c1a237e2562a6e756305d9e"
