pkgname = "bsdm4"
version = "0.99.0"
revision = 0
bootstrap = True
build_style = "gnu_makefile"
make_build_args = ["YACC=byacc", "LEX=true"]
short_desc = "The m4(1) utility from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdm4"
distfiles = [f"https://github.com/chimera-linux/bsdm4/archive/refs/tags/v{version}.tar.gz"]
checksum = ["79169016a8fdfbea2284b5e576807e0e32e46ae98561b57888b7898bf45350c0"]

if not current.bootstrapping:
    hostmakedepends = ["byacc"]

def post_extract(self):
    import shutil
    # pre-bootstrapped copies to avoid dependency cycle with flex
    shutil.copy(self.files_path / "tokenizer.c", self.abs_wrksrc)
    shutil.copy(self.files_path / "tokenizer.h", self.abs_wrksrc)
