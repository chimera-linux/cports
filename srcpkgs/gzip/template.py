pkgname = "gzip"
version = "1.10"
revision = 1
bootstrap = True
build_style = "gnu_configure"
configure_args = [
    "DEFS=NO_ASM", "gl_cv_func_fflush_stdin=yes"
]
short_desc = "GNU compression utility (replacement for compress)"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "https://www.gnu.org/software/gzip/"

from cbuild import sites

distfiles = [f"{sites.gnu}/{pkgname}/{pkgname}-{version}.tar.xz"]
checksum = ["8425ccac99872d544d4310305f915f5ea81e04d0f437ef1a230dc9d1c819d7c0"]

def post_install(self):
    import shutil
    shutil.rmtree(self.destdir / "usr/share/info")
    (self.destdir / "usr/bin/zgrep").unlink()
    (self.destdir / "usr/bin/zegrep").unlink()
    (self.destdir / "usr/bin/zfgrep").unlink()
    (self.destdir / "usr/share/man/man1/zgrep.1").unlink()
