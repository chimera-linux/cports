pkgname = "pahole"
pkgver = "1.25"
pkgrel = 0
build_style = "cmake"
configure_args = ["-D__LIB=lib"]
hostmakedepends = ["cmake", "ninja"]
makedepends = [
    "argp-standalone",
    "elfutils-devel",
    "linux-headers",
    "musl-obstack-devel",
    "zlib-devel",
]
pkgdesc = "Debug information utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/devel/pahole/pahole.git"
source = f"https://fedorapeople.org/~acme/dwarves/dwarves-{pkgver}.tar.xz"
sha256 = "e7d45955f6f4eca25a4c8c3bd6611059b35dc217e45976681d7db170fccdec4a"
# no tests
options = ["!check"]


@subpackage("pahole-devel")
def _devel(self):
    return self.default_devel()
