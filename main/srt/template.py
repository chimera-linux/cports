pkgname = "srt"
pkgver = "1.5.4"
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
sha256 = "d0a8b600fe1b4eaaf6277530e3cfc8f15b8ce4035f16af4a5eb5d4b123640cdd"
hardening = ["vis", "cfi"]
# they really don't want to build
options = ["!check"]


@subpackage("srt-devel")
def _(self):
    return self.default_devel()


@subpackage("srt-progs")
def _(self):
    return self.default_progs()
