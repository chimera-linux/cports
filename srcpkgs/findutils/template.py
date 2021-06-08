pkgname = "findutils"
version = "4.8.0"
revision = 1
bootstrap = True
build_style = "gnu_configure"
configure_args = ["--program-prefix=g"]
short_desc = "GNU Find Utilities"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org/software/findutils"
changelog = "https://git.savannah.gnu.org/cgit/findutils.git/plain/NEWS"

from cbuild import sites

distfiles = [f"{sites.gnu}/{pkgname}/{pkgname}-{version}.tar.xz"]
checksum = ["57127b7e97d91282c6ace556378d5455a9509898297e46e10443016ea1387164"]

alternatives = [
    ("xargs", "xargs", "/usr/bin/gxargs"),
    ("xargs", "xargs.1", "/usr/share/man/man1/gxargs.1"),
    ("find", "find", "/usr/bin/gfind"),
    ("find", "find.1", "/usr/share/man/man1/gfind.1"),
]

def post_configure(self):
    self.make.invoke("dblocation.texi", ["-C", "locate"])
