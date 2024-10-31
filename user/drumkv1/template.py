pkgname = "drumkv1"
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
pkgdesc = "Drum-kit sampler synthesizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://drumkv1.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/drumkv1/drumkv1-{pkgver}.tar.gz"
sha256 = "0c15ecb3b9b44810fd8ca90d58523eb01d392b0c4060648a328a3ea7c9447891"
