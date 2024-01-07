pkgname = "dos2unix"
pkgver = "7.5.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "gettext"]
checkdepends = ["perl"]
pkgdesc = "Line ending converter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://waterlan.home.xs4all.nl/dos2unix.html"
source = f"https://waterlan.home.xs4all.nl/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "da07788bb2e029b0d63f6471d166f68528acd8da2cf14823a188e8a9d5c1fc15"


def post_install(self):
    self.install_license("COPYING.txt")
