pkgname = "parted"
pkgver = "3.8"
pkgrel = 0
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
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/parted"
source = f"$(GNU_SITE)/parted/parted-{pkgver}.tar.xz"
sha256 = "a2b7811f47b0ddb1f7b1d0aa456f7c1270da70708ce231c2fe054c7199eafa63"
# a bunch of environment-based stuff
options = ["!check"]


@subpackage("parted-devel")
def _(self):
    return self.default_devel()


@subpackage("parted-libs")
def _(self):
    return self.default_libs()
