pkgname = "libdatachannel"
pkgver = "0.20.3"
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
sha256 = "31274df211173bec5b3c104559fed25b5466b53f438c050fb71719d53a12c8e7"
hardening = ["cfi", "vis"]
# tests seem to need network access (the tests themselves don't seem to work
# with cfi either; library itself works just fine though)
options = ["!check"]


@subpackage("libdatachannel-devel")
def _devel(self):
    return self.default_devel()
