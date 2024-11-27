pkgname = "cmark"
pkgver = "0.31.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
checkdepends = ["python"]
pkgdesc = "C implementation of the CommonMark markdown specification"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/commonmark/cmark"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3da93db5469c30588cfeb283d9d62edfc6ded9eb0edc10a4f5bbfb7d722ea802"
# defaults to Release which sets this, and the tests crash in an assert without it..
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}


def post_install(self):
    self.install_license("COPYING")


@subpackage("cmark-devel")
def _(self):
    return self.default_devel()


@subpackage("cmark-libs")
def _(self):
    return self.default_libs()
