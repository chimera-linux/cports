pkgname = "lz4"
version = "1.9.3"
revision = 0
build_style = "makefile"
short_desc = "LZ4 compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause, GPL-2.0-or-later"
homepage = "https://lz4.github.io/lz4"
sources = [f"https://github.com/lz4/lz4/archive/v{version}.tar.gz"]
sha256 = ["030644df4611007ff7dc962d981f390361e6c97a34e5cbc393ddfbe019ffe2c1"]

options = ["bootstrap", "!check"]

make_cmd = "gmake"

if not current.bootstrapping:
    hostmakedepends = ["gmake"]

def post_install(self):
    self.install_license("lib/LICENSE")

@subpackage("liblz4")
def _lib(self):
    self.short_desc = "LZ4 compression library"

    return ["usr/lib/*.so.*"]

@subpackage("liblz4-devel")
def _devel(self):
    self.short_decs = "LZ4 compression library - development files"
    self.depends = [f"liblz4={version}-r{revision}"]

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
    ]
