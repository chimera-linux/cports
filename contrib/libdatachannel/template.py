pkgname = "libdatachannel"
pkgver = "0.20.2"
pkgrel = 1
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
sha256 = "8a119064296e8c354f82b6c865306c088ccce0d9863b7cc038927bf10981304e"
hardening = ["cfi", "vis"]
# tests seem to need network access (the tests themselves don't seem to work
# with cfi either; library itself works just fine though)
options = ["!check"]


@subpackage("libdatachannel-devel")
def _devel(self):
    return self.default_devel()
