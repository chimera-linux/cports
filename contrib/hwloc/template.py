pkgname = "hwloc"
pkgver = "2.11.1"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://www.open-mpi.org/projects/hwloc"
source = f"https://www.open-mpi.org/software/hwloc/v{".".join(pkgver.split(".")[0:2])}/downloads/hwloc-{pkgver}.tar.bz2"
sha256 = "04cdfbffad225ce15f66184f0f4141327dabf288d10a8b84d13f517acb7870c6"
# can't run them in bwrap with no sysfs
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("hwloc-devel")
def _(self):
    return self.default_devel()
