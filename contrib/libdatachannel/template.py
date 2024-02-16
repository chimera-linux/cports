pkgname = "libdatachannel"
pkgver = "0.20.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DNO_EXAMPLES=ON",
    "-DNO_TESTS=ON",
    "-DPREFER_SYSTEM_LIB=ON",
    "-DUSE_NICE=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libnice-devel",
    "libsrtp-devel",
    "openssl-devel",
    "plog",
    "usrsctp-devel",
]
pkgdesc = "WebRTC network library"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MPL-2.0"
url = "https://libdatachannel.org"
source = f"https://github.com/paullouisageneau/libdatachannel/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b6f6eaf615b45b1a75feb436ff9836f3d2b7835217b5d2b6d872f209dbb5dc58"
hardening = ["cfi", "vis"]
# needs network access
options = ["!check"]


@subpackage("libdatachannel-devel")
def _devel(self):
    return self.default_devel()
