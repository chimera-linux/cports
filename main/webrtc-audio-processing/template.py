pkgname = "webrtc-audio-processing"
pkgver = "1.3"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dcpp_std=c++17"]
hostmakedepends = ["meson", "pkgconf", "cmake"]
makedepends = ["abseil-cpp-devel", "linux-headers"]
pkgdesc = "Packaging-friendly copy of WebRTC AudioProcessing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://freedesktop.org/software/pulseaudio/webrtc-audio-processing"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "95552fc17faa0202133707bbb3727e8c2cf64d4266fe31bfdb2298d769c1db75"

if self.profile().endian == "big":
    broken = "does not support BE"


def post_install(self):
    self.install_license("COPYING")


@subpackage("webrtc-audio-processing-devel")
def _devel(self):
    return self.default_devel()
