pkgname = "dav1d"
pkgver = "1.5.2"
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
license = "BSD-2-Clause"
url = "https://code.videolan.org/videolan/dav1d"
source = f"{url}/-/archive/{pkgver}/dav1d-{pkgver}.tar.gz"
sha256 = "2fc0810b4cdf72784b3c107827ff10b1d83ec709a1ec1fbdbc6a932daf65ead6"
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
