pkgname = "fortify-headers"
pkgver = "2.2"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "clang"
make_check_args = ["-C", "tests", "run"]
make_use_env = True
hostmakedepends = ["gmake"]
pkgdesc = "Standalone fortify implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://git.2f30.org/fortify-headers"
source = f"https://github.com/jvoisin/fortify-headers/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "127fb933c21ac6e6f426c6405a11ab83d02e97908bc95fba6ac16875ef4772b5"
tool_flags = {"CFLAGS": ["-Wno-macro-redefined"]}
options = ["bootstrap"]


def do_build(self):
    pass
