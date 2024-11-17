pkgname = "fortify-headers"
pkgver = "2.3.3"
pkgrel = 0
build_style = "makefile"
make_check_target = "clang"
make_check_args = ["-C", "tests", "run"]
make_use_env = True
pkgdesc = "Standalone fortify implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://git.2f30.org/fortify-headers"
source = f"https://github.com/jvoisin/fortify-headers/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "26d81fc55b8ce3db22c7a697616392aeba928e921d975053a3f00221d1a33c08"
tool_flags = {"CFLAGS": ["-Wno-macro-redefined"]}
options = ["bootstrap"]


def build(self):
    pass
