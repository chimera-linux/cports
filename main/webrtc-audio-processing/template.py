pkgname = "webrtc-audio-processing"
pkgver = "2.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dcpp_std=c++17"]
hostmakedepends = ["meson", "pkgconf", "cmake"]
makedepends = ["abseil-cpp-devel", "linux-headers"]
pkgdesc = "Packaging-friendly copy of WebRTC AudioProcessing"
license = "BSD-3-Clause"
url = "https://freedesktop.org/software/pulseaudio/webrtc-audio-processing"
source = f"$(FREEDESKTOP_SITE)/pulseaudio/webrtc-audio-processing/webrtc-audio-processing-{pkgver}.tar.gz"
sha256 = "35e86b986d02ea15f3d04741a1a5a735ba399bc0fac0ee089c39480e35fc3253"

if self.profile().endian == "big":
    broken = "does not support BE"


def post_install(self):
    self.install_license("COPYING")


@subpackage("webrtc-audio-processing-devel")
def _(self):
    return self.default_devel()
