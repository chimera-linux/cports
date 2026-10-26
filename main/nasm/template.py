pkgname = "nasm"
pkgver = "3.02"
pkgrel = 0
build_style = "gnu_configure"
# fails to regen
configure_gen = []
make_dir = "."
make_check_target = "test"
hostmakedepends = ["asciidoc"]
makedepends = ["zlib-ng-compat-devel"]
checkdepends = ["perl"]
pkgdesc = "80x86 assembler designed for portability and modularity"
license = "BSD-2-Clause"
url = "https://www.nasm.us"
source = f"{url}/pub/nasm/releasebuilds/{pkgver}/nasm-{pkgver}.tar.xz"
sha256 = "87336eba53b4acfe917424ab5d500d2b0054d9f5148d35c2273ccf2cfb712f0d"
# relies on -fwrapv; clang >= 19 traps on signed overflow anyway
hardening = ["vis", "cfi", "!int"]


def post_install(self):
    self.install_license("LICENSE")
