pkgname = "libaom"
pkgver = "3.8.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DENABLE_TESTS=OFF",
    "-DENABLE_NASM=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "perl",
    "python",
    "nasm",
    "doxygen",
]
makedepends = ["linux-headers"]
pkgdesc = "Reference implementation of the AV1 codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://aomedia.org"
source = [
    f"https://storage.googleapis.com/aom-releases/{pkgname}-{pkgver}.tar.gz"
]
sha256 = ["98f7d6d7ddbf06d088735f5e51782df053fd1b08c553882c2924bd0b2021a202"]
# requires a testdata download, tests take long
options = ["!check"]

tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE"],
    "CXXFLAGS": ["-D_GNU_SOURCE"],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152"],
}

match self.profile().arch:
    case "ppc64":
        configure_args += ["-DENABLE_VSX=0"]
    case "aarch64":
        # requires an explicit assembler
        configure_args += ["-DCMAKE_ASM_COMPILER=clang"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libaom-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libaom-progs")
def _progs(self):
    return self.default_progs()
