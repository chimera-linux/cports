pkgname = "hwloc"
pkgver = "2.12.1"
pkgrel = 1
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
sha256 = "38a90328bb86259f9bb2fe1dc57fd841e111d1e6358012bef23dfd95d21dc66b"
# can't run them in bwrap with no sysfs
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("hwloc-progs")
def _(self):
    # lintcomp: eager preload under different name
    self.options = ["!lintcomp"]

    return self.default_progs(
        extra=["usr/share/applications", "usr/share/hwloc"]
    )


@subpackage("hwloc-devel")
def _(self):
    return self.default_devel()
