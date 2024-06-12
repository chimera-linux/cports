pkgname = "dav1d"
pkgver = "1.4.3"
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
source = f"{url}/-/archive/{pkgver}/dav1d-{pkgver}.tar.gz"
sha256 = "88a023e58d955e0886faf49c72940e0e90914a948a8e60c1326ce3e09e7a6099"
# FIXME cfi, int
hardening = ["vis", "!cfi", "!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("dav1d-devel")
def _devel(self):
    return self.default_devel()


@subpackage("dav1d-progs")
def _progs(self):
    return self.default_progs()
