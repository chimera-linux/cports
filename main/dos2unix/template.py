pkgname = "dos2unix"
pkgver = "7.5.5"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf", "gettext"]
checkdepends = ["perl"]
pkgdesc = "Line ending converter"
license = "BSD-2-Clause"
url = "https://waterlan.home.xs4all.nl/dos2unix.html"
source = f"https://waterlan.home.xs4all.nl/dos2unix/dos2unix-{pkgver}.tar.gz"
sha256 = "75f692b8484c8c24579a2ffd87df16b9c9428ed95497e3393a21d1ba0697ac33"


def post_install(self):
    self.install_license("COPYING.txt")
