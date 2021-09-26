pkgname = "musl-fts"
version = "1.2.7"
revision = 0
build_style = "makefile"
make_build_args = ["PREFIX=/usr"]
short_desc = "Implementation of fts(3) for musl libc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
homepage = "https://github.com/chimera-linux/musl-fts"
distfiles = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{version}-mk2.tar.gz"]
checksum = ["1f65612b523e7040dbd9d5579a2eca97ede79c2ff3f91db7ccc288263e60da50"]

options = ["bootstrap", "!check"]

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
