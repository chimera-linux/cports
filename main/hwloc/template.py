pkgname = "hwloc"
pkgver = "2.12.0"
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
license = "BSD-3-Clause"
url = "https://www.open-mpi.org/projects/hwloc"
source = f"https://www.open-mpi.org/software/hwloc/v{'.'.join(pkgver.split('.')[0:2])}/downloads/hwloc-{pkgver}.tar.bz2"
sha256 = "06a0a2bdc0a5714e839164683846a0e936a896213758e9d37e49e232b89c58d4"
# can't run them in bwrap with no sysfs
# lintcomp: eager preload under different name
options = ["!check", "!lintcomp"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("hwloc-devel")
def _(self):
    return self.default_devel()
