pkgname = "padthv1"
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
sha256 = "da40332357bec28d7478bcd4b72a9cd7cde9b089b9835786dea10327c2542e8f"
