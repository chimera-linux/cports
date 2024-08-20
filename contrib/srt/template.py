pkgname = "srt"
pkgver = "1.5.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DENABLE_UNITTESTS=OFF",
    "-DUSE_ENCLIB=openssl-evp",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gtest-devel",
    "linux-headers",
    "openssl-devel",
]
pkgdesc = "Secure Reliable Transport library"
maintainer = "psykose <alice@ayaya.dev>"
license = "MPL-2.0"
url = "https://www.srtalliance.org"
source = f"https://github.com/Haivision/srt/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "befaeb16f628c46387b898df02bc6fba84868e86a6f6d8294755375b9932d777"
hardening = ["vis", "cfi"]
# they really don't want to build
options = ["!check"]


@subpackage("srt-devel")
def _(self):
    return self.default_devel()


@subpackage("srt-progs")
def _(self):
    return self.default_progs()
