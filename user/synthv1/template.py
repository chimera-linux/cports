pkgname = "synthv1"
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
sha256 = "61e48caee0d4755b69ca423174af9db01fe5420d11d47c08a3153e7592ea682c"
