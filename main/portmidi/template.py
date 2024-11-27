pkgname = "portmidi"
pkgver = "2.0.4"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PortMidi/portmidi"
source = (
    f"https://github.com/PortMidi/portmidi/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "64893e823ae146cabd3ad7f9a9a9c5332746abe7847c557b99b2577afa8a607c"
# vis breaks symbols
hardening = []


def post_install(self):
    self.install_license("license.txt")


@subpackage("portmidi-devel")
def _(self):
    return self.default_devel()
