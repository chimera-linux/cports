pkgname = "dav1d"
pkgver = "1.0.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable_tests=true", "-Denable_asm=true",
    "-Denable_tools=true", "-Dfuzzing_engine=none",
]
hostmakedepends = ["meson", "pkgconf", "nasm"]
pkgdesc = "Small and fast AV1 decoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://code.videolan.org/videolan/dav1d"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "047b8229511a82b5718a1d34c86c067b078efd02f602986d2ed09b23182ec136"
# FIXME cfi, int
hardening = ["vis", "!cfi", "!int"]

@subpackage("dav1d-devel")
def _devel(self):
    return self.default_devel()

@subpackage("dav1d-progs")
def _progs(self):
    return self.default_progs()
