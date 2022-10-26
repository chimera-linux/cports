pkgname = "fortify-headers"
pkgver = "1.1.99"
pkgrel = 0
_gitrev = "6700b691e0e5c3b75225c01c437a06bd598a8343"
build_style = "makefile"
pkgdesc = "Standalone fortify implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://github.com/chimera-linux/fortify-headers"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "7f5ee9d564d6ebfd1a4413a76f9a60b5b7176e5fe19baf3f3b2536449d26f2e0"
# no test suite
options = ["bootstrap", "!check"]

def do_build(self):
    pass
