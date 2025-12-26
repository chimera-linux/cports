pkgname = "fortify-headers"
pkgver = "3.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "clang"
make_check_args = ["-C", "tests", "run"]
make_use_env = True
pkgdesc = "Standalone fortify implementation"
license = "0BSD"
url = "https://git.2f30.org/fortify-headers"
source = f"https://github.com/jvoisin/fortify-headers/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b5fcfbdecfd3942cff16390bd7f9eb2ae7e45c29224309121e0c74a0a81de7ab"
tool_flags = {"CFLAGS": ["-Wno-macro-redefined"]}
options = ["bootstrap"]


def build(self):
    pass
