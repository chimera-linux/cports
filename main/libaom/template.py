pkgname = "libaom"
pkgver = "3.13.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DENABLE_TESTS=OFF",
    "-DENABLE_NASM=ON",
]
hostmakedepends = [
    "cmake",
    "doxygen",
    "nasm",
    "ninja",
    "perl",
    "pkgconf",
    "python",
]
makedepends = ["linux-headers"]
pkgdesc = "Reference implementation of the AV1 codec"
license = "BSD-2-Clause"
url = "https://aomedia.org"
source = f"https://storage.googleapis.com/aom-releases/libaom-{pkgver}.tar.gz"
sha256 = "19e45a5a7192d690565229983dad900e76b513a02306c12053fb9a262cbeca7d"
# requires a testdata download, tests take long
options = ["!check"]

tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE", "-DNDEBUG"],
    "CXXFLAGS": ["-D_GNU_SOURCE", "-DNDEBUG"],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152"],
}

match self.profile().arch:
    case "ppc64":
        configure_args += ["-DENABLE_VSX=0"]
    case "aarch64" | "armv7":
        # requires an explicit assembler
        configure_args += ["-DCMAKE_ASM_COMPILER=clang"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libaom-devel")
def _(self):
    return self.default_devel()


@subpackage("libaom-progs")
def _(self):
    return self.default_progs()
