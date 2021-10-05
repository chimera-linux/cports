pkgname = "musl-fts"
pkgver = "1.2.7"
pkgrel = 0
build_style = "makefile"
make_build_args = ["PREFIX=/usr"]
pkgdesc = "Implementation of fts(3) for musl libc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/musl-fts"
sources = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}-mk2.tar.gz"]
sha256 = ["1f65612b523e7040dbd9d5579a2eca97ede79c2ff3f91db7ccc288263e60da50"]

options = ["bootstrap", "!check", "!lint"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("musl-fts-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/share/man", "usr/include", "usr/lib/*.a", "usr/lib/*.so",
        "usr/lib/pkgconfig"
    ]
