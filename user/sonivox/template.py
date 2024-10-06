pkgname = "sonivox"
pkgver = "3.6.14"
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
sha256 = "216171c5bbe4f5a9524d73a2ee9e7e597c71a040e5d7c9e35b92c9dc459c2985"


@subpackage("sonivox-devel")
def _(self):
    return self.default_devel()
