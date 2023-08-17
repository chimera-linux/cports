pkgname = "srt"
pkgver = "1.5.2"
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
sha256 = "463970a3f575446b3f55abb6f323d5476c963c77b3c975cd902e9c87cdd9a92c"
hardening = ["vis", "cfi"]
# they really don't want to build
options = ["!check"]


@subpackage("srt-devel")
def _devel(self):
    return self.default_devel()


@subpackage("srt-progs")
def _progs(self):
    return self.default_progs()
