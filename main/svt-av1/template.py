pkgname = "svt-av1"
pkgver = "2.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
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
source = f"{url}/-/archive/v{pkgver}/SVT-AV1-v{pkgver}.tar.bz2"
sha256 = "e490d8e8ef8cd1f8f814fd207590f36dc1c1eb228efec959cfea113c57797ced"
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


@subpackage("svt-av1-libs")
def _libs(self):
    return self.default_libs()
