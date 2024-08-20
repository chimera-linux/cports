pkgname = "svt-av1"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_STYLE=Release",
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=OFF",
    "-DENABLE_AVX512=ON",
]
hostmakedepends = [
    "cmake",
    "nasm",
    "ninja",
    "pkgconf",
]
checkdepends = ["python"]
pkgdesc = "AOMedia Scalable Video Technology AV1 Encoder/Decoder"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause-Clear"
url = "https://gitlab.com/AOMediaCodec/SVT-AV1"
source = f"{url}/-/archive/v{pkgver}/SVT-AV1-v{pkgver}.tar.gz"
sha256 = "d5b3094b2583eb9c15705efa92a8b413f01d718ca0adce6826ae1f0f1c69b4fd"
# FIXME int: muloverflow in svt_av1_find_best_sub_pixel_tree for certain encodes
hardening = ["vis", "cfi", "!int"]
# needs patching+clones of a bunch of stuff
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("svt-av1-devel")
def _(self):
    return self.default_devel()


@subpackage("svt-av1-libs")
def _(self):
    return self.default_libs()
