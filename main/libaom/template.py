pkgname = "libaom"
pkgver = "3.3.0"
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
# there are no official tarballs and no deterministic autotarballs
source = [f"https://ftp.octaforge.org/q66/random/{pkgname}-{pkgver}.tar.gz"]
sha256 = ["2538d6f82074f44a1c9d97a2b3984a6c62481b61b06fd4edf959a5a65f88a434"]
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
