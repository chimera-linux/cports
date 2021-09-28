pkgname = "bsdm4"
version = "0.99.1"
revision = 0
build_style = "makefile"
make_build_args = ["YACC=byacc", "LEX=true"]
pkgdesc = "The m4(1) utility from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdm4"
sources = [f"https://github.com/chimera-linux/bsdm4/archive/refs/tags/v{version}.tar.gz"]
sha256 = ["dbe405f94c3dcfd084b97585b270d4b004a4fae26c3c8cf37670e830354a123b"]

options = ["bootstrap", "!check"]

if not current.bootstrapping:
    hostmakedepends = ["byacc"]

def post_patch(self):
    # pre-bootstrapped copies to avoid dependency cycle with flex
    self.cp(self.files_path / "tokenizer.c", ".")
    self.cp(self.files_path / "tokenizer.h", ".")
