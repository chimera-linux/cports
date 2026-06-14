pkgname = "cmark"
pkgver = "0.31.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
checkdepends = ["python"]
renames = ["cmark-libs"]
pkgdesc = "C implementation of the CommonMark markdown specification"
license = "BSD-2-Clause"
url = "https://github.com/commonmark/cmark"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f9bc5ca38bcb0b727f0056100fac4d743e768872e3bacec7746de28f5700d697"
# defaults to Release which sets this, and the tests crash in an assert without it..
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}


def post_install(self):
    self.install_license("COPYING")


@subpackage("cmark-devel")
def _(self):
    return self.default_devel()
