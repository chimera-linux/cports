pkgname = "portmidi"
pkgver = "2.0.6"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
]
pkgdesc = "Cross-platform MIDI input/output library"
license = "MIT"
url = "https://github.com/PortMidi/portmidi"
source = (
    f"https://github.com/PortMidi/portmidi/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "81d22b34051621cd56c8d5ef12908ef2a59764c9cdfba6dae47aabddb71ac914"
# vis breaks symbols
hardening = []


def post_install(self):
    self.install_license("license.txt")


@subpackage("portmidi-devel")
def _(self):
    return self.default_devel()
