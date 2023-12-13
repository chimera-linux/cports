pkgname = "fortify-headers"
pkgver = "2.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "clang"
make_check_args = ["-j1", "-C", "tests", "run"]
make_use_env = True
hostmakedepends = ["gmake"]
checkdepends = ["musl-devel-static", "libunwind-devel-static", "libatomic-chimera-devel-static"]
pkgdesc = "Standalone fortify implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://git.2f30.org/fortify-headers"
source = f"https://github.com/jvoisin/fortify-headers/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a7d6c8b37b8deccac4320047acec8f0f77050df975ec758fa05be25a7a289c99"
tool_flags = {"CFLAGS": ["-Wno-macro-redefined"]}
options = ["bootstrap"]


def do_build(self):
    pass
