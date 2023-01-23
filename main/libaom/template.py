pkgname = "libaom"
pkgver = "3.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DENABLE_TESTS=OFF"]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "perl", "python", "yasm", "doxygen"
]
makedepends = ["linux-headers"]
pkgdesc = "Reference implementation of the AV1 codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://aomedia.org"
source = [f"https://storage.googleapis.com/aom-releases/{pkgname}-{pkgver}.tar.gz"]
sha256 = ["d37dbee372e2430a7efde813984ae6d78bdf1fc4080ebe32457c9115408b0738"]
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
