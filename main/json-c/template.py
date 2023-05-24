pkgname = "json-c"
pkgver = "0.16"
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
sha256 = "8e45ac8f96ec7791eaf3bb7ee50e9c2100bbbc87b8d0f1d030c5ba8a0288d96b"
tool_flags = {"CFLAGS": ["-Wno-error"]}


def post_install(self):
    self.install_license("COPYING")


@subpackage("json-c-devel")
def _devel(self):
    return self.default_devel()
