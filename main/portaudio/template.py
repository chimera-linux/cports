pkgname = "portaudio"
pkgver = "19.7.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "linux-headers",
    "pipewire-jack-devel",
]
pkgdesc = "C library for real-time audio i/o"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://www.portaudio.com"
source = (
    f"https://github.com/PortAudio/portaudio/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "5af29ba58bbdbb7bbcefaaecc77ec8fc413f0db6f4c4e286c40c3e1b83174fa0"
# vis breaks symbols
hardening = []
# tests need hardware
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("portaudio-devel")
def _(self):
    return self.default_devel()
