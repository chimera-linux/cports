pkgname = "webrtc-audio-processing"
pkgver = "0.3.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Packaging-friendly copy of WebRTC AudioProcessing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://freedesktop.org/software/pulseaudio/webrtc-audio-processing"
source = f"{url}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a0fdd938fd85272d67e81572c5a4d9e200a0c104753cb3c209ded175ce3c5dbf"

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("COPYING")

@subpackage("webrtc-audio-processing-static")
def _static(self):
    return self.default_static()

@subpackage("webrtc-audio-processing-devel")
def _devel(self):
    return self.default_devel()
