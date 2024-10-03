pkgname = "padthv1"
pkgver = "1.1.2"
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
sha256 = "17fdbadc2114d3f460214d7b1c1a11e7e7c5d638f3ef522674f96a2dd2eb3a06"
