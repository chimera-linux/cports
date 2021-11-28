pkgname = "yasm"
pkgver = "1.3.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["xmlto", "python"]
pkgdesc = "Complete rewrite of the NASM assembler"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND BSD-3-Clause AND (Artistic-1.0 OR GPL-2.0-or-later OR LGPL-2.1-or-later)"
url = "http://www.tortall.net/projects/yasm"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "3dce6601b495f5b3d45b59f7d2492a340ee7e84b5beca17e48f862502bd5603f"
options = ["lto"]

def post_install(self):
    self.rm(self.destdir / "usr/lib", recursive = True)
    self.rm(self.destdir / "usr/include", recursive = True)

    self.install_license("COPYING")
    self.install_license("BSD.txt")
    self.install_license("Artistic.txt")
