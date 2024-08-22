pkgname = "dos2unix"
pkgver = "7.5.2"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf", "gettext"]
checkdepends = ["perl"]
pkgdesc = "Line ending converter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://waterlan.home.xs4all.nl/dos2unix.html"
source = f"https://waterlan.home.xs4all.nl/dos2unix/dos2unix-{pkgver}.tar.gz"
sha256 = "264742446608442eb48f96c20af6da303cb3a92b364e72cb7e24f88239c4bf3a"


def post_install(self):
    self.install_license("COPYING.txt")
