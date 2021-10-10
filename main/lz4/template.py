pkgname = "lz4"
pkgver = "1.9.3"
pkgrel = 0
build_style = "makefile"
pkgdesc = "LZ4 compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND GPL-2.0-or-later"
url = "https://lz4.github.io/lz4"
source = f"https://github.com/lz4/lz4/archive/v{pkgver}.tar.gz"
sha256 = "030644df4611007ff7dc962d981f390361e6c97a34e5cbc393ddfbe019ffe2c1"

options = ["bootstrap", "!check", "!lint"]

make_cmd = "gmake"

if not current.bootstrapping:
    hostmakedepends = ["pkgconf", "gmake"]

def post_install(self):
    self.install_license("lib/LICENSE")

@subpackage("liblz4")
def _lib(self):
    self.pkgdesc = "LZ4 compression library"

    return ["usr/lib/*.so.*"]

@subpackage("liblz4-devel")
def _devel(self):
    self.short_decs = "LZ4 compression library (development files)"
    self.depends = [f"liblz4={pkgver}-r{pkgrel}"]

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
    ]
