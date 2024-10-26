pkgname = "libdatachannel"
pkgver = "0.22.2"
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
sha256 = "8431ba62a3c83fbee05257226fb8bcb256b1a5ce48b449a718e3be5dbe9b2226"
hardening = ["cfi", "vis"]
# tests seem to need network access (the tests themselves don't seem to work
# with cfi either; library itself works just fine though)
options = ["!check"]


@subpackage("libdatachannel-devel")
def _(self):
    return self.default_devel()
