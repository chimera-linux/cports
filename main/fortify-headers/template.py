pkgname = "fortify-headers"
pkgver = "2.3.1"
pkgrel = 1
build_style = "makefile"
make_check_target = "clang"
make_check_args = ["-C", "tests", "run"]
make_use_env = True
pkgdesc = "Standalone fortify implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://git.2f30.org/fortify-headers"
source = f"https://github.com/jvoisin/fortify-headers/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "531a029fb5ff3c266f472d0aad74f750a40e15d476cf80c67ffb39c07f34a0a7"
tool_flags = {"CFLAGS": ["-Wno-macro-redefined"]}
options = ["bootstrap"]


def build(self):
    pass
