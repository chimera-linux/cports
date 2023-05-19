pkgname = "webrtc-audio-processing-0.3"
pkgver = "0.3.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Packaging-friendly copy of WebRTC AudioProcessing (0.3.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://freedesktop.org/software/pulseaudio/webrtc-audio-processing"
source = f"{url}/webrtc-audio-processing-{pkgver}.tar.xz"
sha256 = "a0fdd938fd85272d67e81572c5a4d9e200a0c104753cb3c209ded175ce3c5dbf"

def post_install(self):
    self.install_license("COPYING")

@subpackage("webrtc-audio-processing-0.3-devel")
def _devel(self):
    return self.default_devel()
