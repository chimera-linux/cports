pkgname = "sonivox"
pkgver = "3.6.15"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SONIVOX_STATIC=OFF", "-DBUILD_TESTING=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "MIDI synthesizer library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/pedrolcl/sonivox"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3e54cf11ecdc7ffd9fb24f0ba3319b6e0fe3df56f5e3082f2847666a31be3ff3"


@subpackage("sonivox-devel")
def _(self):
    return self.default_devel()
