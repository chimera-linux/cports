pkgname = "lz4"
pkgver = "1.9.3"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf", "gmake"]
pkgdesc = "LZ4 compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND GPL-2.0-or-later"
url = "https://lz4.github.io/lz4"
source = f"https://github.com/lz4/lz4/archive/v{pkgver}.tar.gz"
sha256 = "030644df4611007ff7dc962d981f390361e6c97a34e5cbc393ddfbe019ffe2c1"
options = ["bootstrap"]

def post_install(self):
    self.install_license("lib/LICENSE")

@subpackage("liblz4")
def _lib(self):
    self.pkgdesc = "LZ4 compression library"

    return self.default_libs()

@subpackage("liblz4-devel")
def _devel(self):
    self.short_decs = "LZ4 compression library (development files)"

    return self.default_devel()
