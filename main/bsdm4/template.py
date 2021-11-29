pkgname = "bsdm4"
pkgver = "0.99.1"
pkgrel = 0
build_style = "makefile"
make_build_args = ["YACC=byacc", "LEX=true"]
hostmakedepends = ["byacc"]
pkgdesc = "FreeBSD m4(1) utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdm4"
source = f"https://github.com/chimera-linux/bsdm4/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dbe405f94c3dcfd084b97585b270d4b004a4fae26c3c8cf37670e830354a123b"
# no test suite
options = ["bootstrap", "!check"]

def post_patch(self):
    # pre-bootstrapped copies to avoid dependency cycle with flex
    self.cp(self.files_path / "tokenizer.c", ".")
    self.cp(self.files_path / "tokenizer.h", ".")
