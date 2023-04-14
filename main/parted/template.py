pkgname = "parted"
pkgver = "3.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
# TODO: look into porting to editline properly
# it compiles if forced, but fails extra tests
makedepends = [
    "libuuid-devel", "libblkid-devel", "ncurses-devel", "readline-devel",
    "device-mapper-devel", "linux-headers"
]
checkdepends = ["e2fsprogs", "perl", "python"]
pkgdesc = "GNU parted"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/parted"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3b43dbe33cca0f9a18601ebab56b7852b128ec1a3df3a9b30ccde5e73359e612"
# a bunch of environment-based stuff
options = ["!check"]

@subpackage("parted-devel")
def _devel(self):
    return self.default_devel()

@subpackage("parted-libs")
def _progs(self):
    return self.default_libs()
