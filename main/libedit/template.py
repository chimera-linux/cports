pkgname = "libedit"
_datever = "20210910"
_distver = 3.1
pkgver = f"{_datever}.{_distver}"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel"]
pkgdesc = "Port of the NetBSD command line editing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.thrysoee.dk/editline"
source = f"http://thrysoee.dk/editline/{pkgname}-{_datever}-{_distver}.tar.gz"
sha256 = "6792a6a992050762edcca28ff3318cdb7de37dccf7bc30db59fcd7017eed13c5"
options = ["bootstrap"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libedit-static")
def _static(self):
    return self.default_static()

@subpackage("libedit-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()
