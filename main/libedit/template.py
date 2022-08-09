pkgname = "libedit"
pkgver = f"20220411"
pkgrel = 0
_gitrev = "167194266af260f623021284184511b598c50f87"
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Port of the NetBSD command line editing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/chimera-linux/libedit-chimera"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "f7dc1e03ed0c0abf6d839950deff01555c10320c8fb59d6273e8bfedebff461c"
options = ["bootstrap"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libedit-devel")
def _devel(self):
    return self.default_devel()
