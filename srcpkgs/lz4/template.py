pkgname = "lz4"
version = "1.9.3"
revision = 0
bootstrap = True
build_style = "gnu_makefile"
short_desc = "LZ4 compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause, GPL-2.0-or-later"
homepage = "https://lz4.github.io/lz4"
changelog = "https://raw.githubusercontent.com/lz4/lz4/dev/NEWS"
distfiles = [f"https://github.com/lz4/lz4/archive/v{version}.tar.gz"]
checksum = ["030644df4611007ff7dc962d981f390361e6c97a34e5cbc393ddfbe019ffe2c1"]

make_cmd = "gmake"

if not current.bootstrapping:
    hostmakedepends = ["gmake"]

def post_install(self):
    self.install_license("lib/LICENSE")

@subpackage("liblz4")
def _lib(self):
    self.short_desc = "LZ4 compression library"

    def install():
        self.take("usr/lib/*.so.*")

    return install

@subpackage("liblz4-devel")
def _devel(self):
    self.short_decs = "LZ4 compression library - development files"
    self.depends = [f"liblz4={version}-r{revision}"]

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/lib/pkgconfig")

    return install
