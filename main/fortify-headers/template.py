pkgname = "fortify-headers"
pkgver = "1.1.99"
pkgrel = 0
_gitrev = "55ae3986e7c54efdbcb4b3d9e5834ed4826d81f7"
build_style = "makefile"
pkgdesc = "Standalone fortify implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://github.com/chimera-linux/fortify-headers"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "c7eb4e1b442dfcf9f85862851bd5dd3f43b7f879a7755820be4e04560d3ce2c0"
# no test suite
options = ["bootstrap", "!check"]


def do_build(self):
    pass
