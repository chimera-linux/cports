pkgname = "zstd"
version = "1.5.0"
revision = 1
bootstrap = True
makedepends = ["zlib-devel", "liblzma-devel", "liblz4-devel"]
checkdepends = ["gtest-devel"]
short_desc = "Fast real-time compression algorithm - CLI tool"
maintainer = "Orphaned <orphan@voidlinux.org>"
license = "BSD-3-Clause, GPL-2.0-or-later"
homepage = "http://www.zstd.net"
distfiles = [f"https://github.com/facebook/zstd/releases/download/v{version}/zstd-{version}.tar.gz"]
checksum = ["5194fbfa781fcf45b98c5e849651aa7b3b0a008c6b72d4a0db760f3002291e94"]

def init_build(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_build(self):
    self.make.invoke("lib-mt")
    self.make.build(["-C", "contrib/pzstd"])

def do_install(self):
    self.make.install(["PREFIX=/usr"])
    self.make.install(["-C", "contrib/pzstd", "PREFIX=/usr"])
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
        "usr/lib/*.so",
        "usr/lib/*.a"
    ]
