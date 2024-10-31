pkgname = "synthv1"
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
pkgdesc = "Polyphonic synthesizer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://synthv1.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/synthv1/synthv1-{pkgver}.tar.gz"
sha256 = "b1398766153f183828bbfde119b84cb70198a8c65554ef4a92e9fe458367f271"
