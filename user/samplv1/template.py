pkgname = "samplv1"
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
sha256 = "2d3b810a51c1a54626d93e5a963317c40973519b78bbc3c9a8e6cb59114ecad1"
