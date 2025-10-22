pkgname = "sonivox"
pkgver = "3.6.16"
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
license = "Apache-2.0"
url = "https://github.com/pedrolcl/sonivox"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8e9adf39a5e60c5b9ce4d1b79c83680cfab97d6e8eec6ffb6a3d0bad41413531"


@subpackage("sonivox-devel")
def _(self):
    return self.default_devel()
