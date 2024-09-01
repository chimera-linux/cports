pkgname = "synthv1"
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
pkgdesc = "Polyphonic synthesizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://synthv1.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/synthv1/synthv1-{pkgver}.tar.gz"
sha256 = "e3ae0b32624d6d782a0bf30b8cf70b1a6b92a79ed99f72966cecf8c7d31df46b"
