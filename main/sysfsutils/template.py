pkgname = "sysfsutils"
pkgver = "2.1.1"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Utilities to deal with sysfs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-or-later"
url = "http://linux-diag.sourceforge.net/Sysfsutils.html"
source = f"https://github.com/linux-ras/sysfsutils/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f7f669d27c997d3eb3f3e014b4c0aa1aa4d07ce4d6f9e41fa835240f2bf38810"


@subpackage("sysfsutils-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libsysfs")]

    return self.default_libs()


@subpackage("sysfsutils-devel")
def _(self):
    return self.default_devel()
