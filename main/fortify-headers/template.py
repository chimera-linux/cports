pkgname = "fortify-headers"
pkgver = "3.0.1"
pkgrel = 0
build_style = "makefile"
make_check_target = "clang"
make_check_args = ["-C", "tests", "run"]
make_use_env = True
pkgdesc = "Standalone fortify implementation"
license = "0BSD"
url = "https://git.2f30.org/fortify-headers"
source = f"https://github.com/jvoisin/fortify-headers/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "576ac1dc2db9a503d8458c1e9f4a6ce8b0437cfc3c507859d7601a3b8d8ac0e6"
tool_flags = {"CFLAGS": ["-Wno-macro-redefined"]}
options = ["bootstrap"]


def build(self):
    pass
