pkgname = "libstatgrab"
pkgver = "0.92.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "ncurses-devel",
]
checkdepends = ["perl"]
pkgdesc = "Cross-platform library for system statistics"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://libstatgrab.org"
source = f"https://github.com/libstatgrab/libstatgrab/releases/download/LIBSTATGRAB_{pkgver.replace('.', '_')}/libstatgrab-{pkgver}.tar.gz"
sha256 = "5688aa4a685547d7174a8a373ea9d8ee927e766e3cc302bdee34523c2c5d6c11"


@subpackage("libstatgrab-devel")
def _(self):
    return self.default_devel()
