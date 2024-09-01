pkgname = "sonivox"
pkgver = "3.6.12"
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
sha256 = "23a7f29c617e791dfcb50b75eef41464e4bf3fca15b19da395a64373ff5d8456"


@subpackage("sonivox-devel")
def _(self):
    return self.default_devel()
