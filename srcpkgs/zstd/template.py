pkgname = "zstd"
version = "1.5.0"
revision = 1
bootstrap = True
build_style = "meson"
makedepends = ["zlib-devel", "liblzma-devel", "liblz4-devel"]
checkdepends = ["gtest-devel"]
configure_args = [
    "-Dzlib=enabled", "-Dlzma=enabled", "-Dlz4=enabled", "-Dbin_contrib=true"
]
short_desc = "Fast real-time compression algorithm - CLI tool"
maintainer = "q66 <daniel@octaforge.org>"
license = "BSD-3-Clause"
homepage = "http://www.zstd.net"
distfiles = [f"https://github.com/facebook/zstd/releases/download/v{version}/zstd-{version}.tar.gz"]
checksum = ["5194fbfa781fcf45b98c5e849651aa7b3b0a008c6b72d4a0db760f3002291e94"]

meson_dir = "build/meson"

if not current.bootstrapping:
    hostmakedepends = ["pkgconf", "meson"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libzstd")
def _lib(self):
    self.short_desc = "Fast real-time compression algorithm"

    return ["usr/lib/*.so.*"]

@subpackage("libzstd-devel")
def _devel(self):
    self.short_desc = "Fast real-time compression algorithm - development files"
    self.depends = [f"libzstd-{version}_{revision}"]

    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.so"
    ]
