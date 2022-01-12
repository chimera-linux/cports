pkgname = "libaom"
pkgver = "3.2.0"
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
source = [f"https://aomedia.googlesource.com/aom/+archive/v{pkgver}.tar.gz"]
sha256 = ["3d618b65eb601c348a10ef375dc6a72fe4c94d702a0ca4be1b268ffcf9c46609"]
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
# requires a testdata download, tests take long
options = ["!check"]

match self.profile().arch:
    case "ppc64":
        configure_args += ["-DENABLE_VSX=0"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libaom-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libaom-progs")
def _progs(self):
    return self.default_progs()
