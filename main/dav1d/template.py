pkgname = "dav1d"
pkgver = "1.2.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable_tests=true",
    "-Denable_asm=true",
    "-Denable_tools=true",
    "-Dfuzzing_engine=none",
]
hostmakedepends = ["meson", "pkgconf", "nasm"]
pkgdesc = "Small and fast AV1 decoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://code.videolan.org/videolan/dav1d"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "2dd85860d213479672b1c708e31593446e8c2b53ff41e2ca25a2eafb718424e2"
# FIXME cfi, int
hardening = ["vis", "!cfi", "!int"]


@subpackage("dav1d-devel")
def _devel(self):
    return self.default_devel()


@subpackage("dav1d-progs")
def _progs(self):
    return self.default_progs()
