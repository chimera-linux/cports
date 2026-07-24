pkgname = "hwloc"
pkgver = "2.14.0"
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
sha256 = "966b9bb3e9f29f8d65ce8d106779e457f40e246a645e584b100772a42f9ae94b"
# can't run them in bwrap with no sysfs
# lintcomp: eager preload under different name
options = ["!check", "!lintcomp"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("hwloc-libs")
def _(self):
    return self.default_libs()


@subpackage("hwloc-devel")
def _(self):
    return self.default_devel()
