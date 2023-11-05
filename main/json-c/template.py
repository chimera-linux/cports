pkgname = "json-c"
pkgver = "0.17"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_THREADING=ON",
    "-DBUILD_STATIC_LIBS=ON",
    "-DDISABLE_WERROR=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "doxygen"]
pkgdesc = "JSON implementation in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://json-c.github.io/json-c"
source = f"https://s3.amazonaws.com/json-c_releases/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "7550914d58fb63b2c3546f3ccfbe11f1c094147bd31a69dcd23714d7956159e6"
tool_flags = {"CFLAGS": ["-Wno-error"]}
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("json-c-devel")
def _devel(self):
    return self.default_devel()
