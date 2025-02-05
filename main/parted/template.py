pkgname = "parted"
pkgver = "3.6"
pkgrel = 2
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
# TODO: look into porting to editline properly
# it compiles if forced, but fails extra tests
makedepends = [
    "linux-headers",
    "lvm2-devel",
    "ncurses-devel",
    "readline-devel",
    "util-linux-blkid-devel",
    "util-linux-uuid-devel",
]
checkdepends = ["e2fsprogs", "perl", "python"]
pkgdesc = "GNU parted"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/parted"
source = f"$(GNU_SITE)/parted/parted-{pkgver}.tar.xz"
sha256 = "3b43dbe33cca0f9a18601ebab56b7852b128ec1a3df3a9b30ccde5e73359e612"
# a bunch of environment-based stuff
options = ["!check"]


@subpackage("parted-devel")
def _(self):
    return self.default_devel()


@subpackage("parted-libs")
def _(self):
    return self.default_libs()
