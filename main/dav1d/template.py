pkgname = "dav1d"
pkgver = "1.5.0"
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
sha256 = "78b15d9954b513ea92d27f39362535ded2243e1b0924fde39f37a31ebed5f76b"
# FIXME cfi, int
hardening = ["vis", "!cfi", "!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("dav1d-devel")
def _(self):
    return self.default_devel()


@subpackage("dav1d-progs")
def _(self):
    return self.default_progs()
