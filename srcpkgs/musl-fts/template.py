pkgname = "musl-fts"
version = "1.2.7"
revision = 1
wrksrc = f"musl-fts-{version}-mk"
bootstrap = True
build_style = "gnu_makefile"
make_build_args = ["PREFIX=/usr"]
short_desc = "Implementation of fts(3) for musl libc"
maintainer = "q66 <daniel@octaforge.org>"
license = "BSD-3-Clause"
homepage = "https://github.com/chimera-linux/musl-fts"
distfiles = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{version}-mk.tar.gz"]
checksum = ["6422f2bf36abf4e2e5dac53b8e3318f23359ba9eb459e412f91553e9815b6661"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("musl-fts-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"{pkgname}={version}-r{revision}"]

    return [
        "usr/share/man", "usr/include", "usr/lib/*.a", "usr/lib/*.so",
        "usr/lib/pkgconfig"
    ]
