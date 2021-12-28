pkgname = "json-c"
pkgver = "0.15"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_THREADING=ON", "-DBUILD_STATIC_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "doxygen"]
pkgdesc = "JSON implementation in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://json-c.github.io/json-c"
source = f"https://s3.amazonaws.com/json-c_releases/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "b8d80a1ddb718b3ba7492916237bbf86609e9709fb007e7f7d4322f02341a4c6"
tool_flags = {"CFLAGS": ["-Wno-error"]}

def post_install(self):
    self.install_license("COPYING")

@subpackage("json-c-devel")
def _devel(self):
    return self.default_devel()
