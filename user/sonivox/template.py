pkgname = "sonivox"
pkgver = "3.6.13"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SONIVOX_STATIC=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "MIDI synthesizer library"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/pedrolcl/sonivox"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c5c088acc423a78f7ec103f3d99c7b16c85301c2969dcebdc49537c7247790c4"


@subpackage("sonivox-devel")
def _(self):
    return self.default_devel()
