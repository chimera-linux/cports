pkgname = "dos2unix"
pkgver = "7.5.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "gettext-tiny"]
checkdepends = ["perl"]
pkgdesc = "Line ending converter"
license = "BSD-2-Clause"
url = "https://waterlan.home.xs4all.nl/dos2unix.html"
source = f"https://waterlan.home.xs4all.nl/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "7a3b01d01e214d62c2b3e04c3a92e0ddc728a385566e4c0356efa66fd6eb95af"


def post_install(self):
    self.install_license("COPYING.txt")
