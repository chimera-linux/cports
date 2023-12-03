pkgname = "noise-suppression-for-voice"
pkgver = "1.03"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_AU_PLUGIN=OFF",
    "-DBUILD_AUV3_PLUGIN=OFF",
    "-DBUILD_LV2_PLUGIN=OFF",
    "-DBUILD_VST_PLUGIN=OFF",
    "-DBUILD_VST3_PLUGIN=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Noise suppression plugin based on RNNoise"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/werman/noise-suppression-for-voice"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8c85cae3ebbb3a18facc38930a3b67ca90e3ad609526a0018c71690de35baf04"
# tests ftbfs
options = ["!check"]
