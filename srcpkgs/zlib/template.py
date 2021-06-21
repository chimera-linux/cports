pkgname = "zlib"
version = "1.2.11"
revision = 3
bootstrap = True
build_style = "configure"
short_desc = "Compression/decompression Library"
maintainer = "Orphaned <orphan@voidlinux.org>"
license = "Zlib"
homepage = "http://www.zlib.net"
distfiles = [f"{homepage}/{pkgname}-{version}.tar.gz"]
checksum = ["c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1"]

def do_configure(self):
    self.do(self.chroot_wrksrc / "configure", [
        "--prefix=/usr", "--shared"
    ], build = True, env = {
        "LDFLAGS": "",
        "LDSHAREDLIBC": ""
    })

@subpackage("zlib-devel")
def _devel(self):
    self.depends = [f"zlib={version}-r{revision}"]
    self.short_desc = short_desc + " - development files"

    def install():
        self.take("usr/include")
        self.take("usr/lib/pkgconfig")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/share")

    return install
