pkgname = "musl-rpmatch"
pkgver = "1.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["PREFIX=/usr"]
pkgdesc = "Implementation of rpmatch(3) for musl libc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/musl-rpmatch"
sources = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}-mk2.tar.gz"]
sha256 = ["a7b9649b49a8a59da09cf61228dc812cae6f0aea8be036788a9173c6f15a1a77"]

options = ["bootstrap", "!check", "!lint"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("musl-rpmatch-devel")
def _devel(self):
    self.pkgdesc = pkgdesc + " - development files"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/include", "usr/lib/*.a", "usr/lib/*.so",
        "usr/lib/pkgconfig"
    ]
