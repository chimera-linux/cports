pkgname = "bsdm4"
version = "0.99.1"
revision = 0
build_style = "gnu_makefile"
make_build_args = ["YACC=byacc", "LEX=true"]
short_desc = "The m4(1) utility from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdm4"
distfiles = [f"https://github.com/chimera-linux/bsdm4/archive/refs/tags/v{version}.tar.gz"]
checksum = ["dbe405f94c3dcfd084b97585b270d4b004a4fae26c3c8cf37670e830354a123b"]

options = ["bootstrap"]

if not current.bootstrapping:
    hostmakedepends = ["byacc"]

def post_extract(self):
    import shutil
    # pre-bootstrapped copies to avoid dependency cycle with flex
    shutil.copy(self.files_path / "tokenizer.c", self.abs_wrksrc)
    shutil.copy(self.files_path / "tokenizer.h", self.abs_wrksrc)
