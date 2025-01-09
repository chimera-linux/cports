pkgname = "hwloc"
pkgver = "2.11.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "libxml2-devel",
    "ncurses-devel",
    "udev-devel",
]
pkgdesc = "Hardware resource locality library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.open-mpi.org/projects/hwloc"
source = f"https://www.open-mpi.org/software/hwloc/v{'.'.join(pkgver.split('.')[0:2])}/downloads/hwloc-{pkgver}.tar.bz2"
sha256 = "f7f88fecae067100f1a1a915b658add0f4f71561259482910a69baea22fe8409"
# can't run them in bwrap with no sysfs
# lintcomp: eager preload under different name
options = ["!check", "!lintcomp"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("hwloc-devel")
def _(self):
    return self.default_devel()
