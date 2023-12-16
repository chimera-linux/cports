pkgname = "fortify-headers"
pkgver = "2.1"
pkgrel = 0
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
sha256 = "12e43fd91ee0327c5f0611b72b6f2e2d4b93fae289a80e059104ef2c4801c622"
tool_flags = {"CFLAGS": ["-Wno-macro-redefined"]}
options = ["bootstrap"]


def do_build(self):
    pass
