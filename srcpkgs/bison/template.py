pkgname = "bison"
version = "3.7.6"
revision = 1
build_style = "gnu_configure"
hostmakedepends = ["perl", "m4"]
depends = ["m4"]
checkdepends = ["autoconf", "flex"]
short_desc = "GNU yacc(1) replacement"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org/software/bison/bison.html"

from cbuild import sites

distfiles = [f"{sites.gnu}/bison/bison-{version}.tar.xz"]
checksum = ["67d68ce1e22192050525643fc0a7a22297576682bef6a5c51446903f5aeef3cf"]

alternatives = [
    ("yacc", "yacc", "/usr/bin/bison-yacc"),
    ("yacc", "yacc.1", "/usr/share/man/man1/bison-yacc.1")
]

disable_parallel_build = True

def post_install(self):
    import os
    os.rename(
        self.destdir / "usr/bin/yacc",
        self.destdir / "usr/bin/bison-yacc"
    )
    os.rename(
        self.destdir / "usr/share/man/man1/yacc.1",
        self.destdir / "usr/share/man/man1/bison-yacc.1"
    )
