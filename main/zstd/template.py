pkgname = "zstd"
pkgver = "1.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["pkgconf", "meson"]
makedepends = ["zlib-devel", "liblzma-devel", "liblz4-devel"]
checkdepends = ["gtest-devel"]
configure_args = [
    "-Dzlib=enabled", "-Dlzma=enabled", "-Dlz4=enabled", "-Dbin_contrib=true"
]
pkgdesc = "Fast real-time compression algorithm - CLI tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
homepage = "http://www.zstd.net"
sources = [f"https://github.com/facebook/zstd/releases/download/v{pkgver}/zstd-{pkgver}.tar.gz"]
sha256 = ["5194fbfa781fcf45b98c5e849651aa7b3b0a008c6b72d4a0db760f3002291e94"]

options = ["!check"]
meson_dir = "build/meson"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libzstd")
def _lib(self):
    self.pkgdesc = "Fast real-time compression algorithm"

    return ["usr/lib/*.so.*"]

@subpackage("libzstd-devel")
def _devel(self):
    self.pkgdesc = "Fast real-time compression algorithm - development files"
    self.depends = [f"libzstd={pkgver}-r{pkgrel}"]

    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.so",
        "usr/lib/*.a"
    ]
