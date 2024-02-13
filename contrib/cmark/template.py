pkgname = "cmark"
pkgver = "0.31.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://github.com/commonmark/cmark"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bbcb8f8c03b5af33fcfcf11a74e9499f20a9043200b8552f78a6e8ba76e04d11"
# defaults to Release which sets this, and the tests crash in an assert without it..
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}


def post_install(self):
    self.install_license("COPYING")


@subpackage("cmark-devel")
def _devel(self):
    return self.default_devel()


@subpackage("cmark-libs")
def _libs(self):
    return self.default_libs()
