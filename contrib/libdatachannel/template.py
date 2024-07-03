pkgname = "libdatachannel"
pkgver = "0.21.2"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MPL-2.0"
url = "https://libdatachannel.org"
source = f"https://github.com/paullouisageneau/libdatachannel/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ffaa8cc36722726227757d9052634a0dab23953d0d919d5c82b732b53cbd0879"
hardening = ["cfi", "vis"]
# tests seem to need network access (the tests themselves don't seem to work
# with cfi either; library itself works just fine though)
options = ["!check"]


@subpackage("libdatachannel-devel")
def _devel(self):
    return self.default_devel()
