pkgname = "samplv1"
pkgver = "1.1.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "liblo-devel",
    "libsndfile-devel",
    "lv2",
    "pipewire-jack-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "Polyphonic sampler synthesizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://samplv1.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/samplv1/samplv1-{pkgver}.tar.gz"
sha256 = "93735b4053298865eb44a363d2c3b6c61e13376560d0f1fb45ff555f132a0b1b"
