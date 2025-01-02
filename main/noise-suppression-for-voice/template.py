pkgname = "noise-suppression-for-voice"
pkgver = "1.10"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_AU_PLUGIN=OFF",
    "-DBUILD_AUV3_PLUGIN=OFF",
    "-DBUILD_LV2_PLUGIN=OFF",
    "-DBUILD_VST_PLUGIN=OFF",
    "-DBUILD_VST3_PLUGIN=OFF",
    "-DBUILD_TESTS=OFF",
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
sha256 = "6e0c11aeb8392891750b0243c2ba695dab07654bf3f4e01adbed927b36cc690a"
# tests ftbfs
options = ["!check"]
