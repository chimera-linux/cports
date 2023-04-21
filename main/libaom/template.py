pkgname = "libaom"
pkgver = "3.6.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON", "-DENABLE_TESTS=OFF", "-DENABLE_NASM=ON"
]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "perl", "python", "nasm", "doxygen"
]
makedepends = ["linux-headers"]
pkgdesc = "Reference implementation of the AV1 codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://aomedia.org"
source = [f"https://storage.googleapis.com/aom-releases/{pkgname}-{pkgver}.tar.gz"]
sha256 = ["a4a6c0fab685da743b796662a928fcdf7ae60594edc306efb73e78a17ea6cde6"]
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
# requires a testdata download, tests take long
options = ["!check"]

match self.profile().arch:
    case "ppc64":
        configure_args += ["-DENABLE_VSX=0"]
    case "aarch64":
        # requires an explicit assembler
        configure_args += ["-DAS_EXECUTABLE=clang"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libaom-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libaom-progs")
def _progs(self):
    return self.default_progs()
