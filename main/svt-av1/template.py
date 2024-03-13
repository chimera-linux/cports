pkgname = "svt-av1"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=OFF",
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
source = f"https://gitlab.com/AOMediaCodec/SVT-AV1/-/archive/v{pkgver}/SVT-AV1-v{pkgver}.tar.bz2"
sha256 = "f9c076c377e504be15e195db8dd36d91233bc37cb8e82530382f38bc1926df02"
# FIXME int: muloverflow in svt_av1_find_best_sub_pixel_tree for certain encodes
hardening = ["vis", "cfi", "!int"]
# needs patching+clones of a bunch of stuff
options = ["!check"]

tool_flags = {
    # DNDEBUG to disarm NDEBUG checks (as Release always sets)
    # O3 for encoder
    "CFLAGS": ["-DNDEBUG", "-O3"],
    "CXXFLAGS": ["-DNDEBUG", "-O3"],
}


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("svt-av1-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libsvtav1dec")
def _dec(self):
    return ["usr/lib/libSvtAv1Dec.so.*"]


@subpackage("libsvtav1enc")
def _enc(self):
    return ["usr/lib/libSvtAv1Enc.so.*"]
