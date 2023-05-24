pkgname = "libdaemon"
pkgver = "0.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-lynx"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Lightweight C library that eases the writing of UNIX daemons"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://0pointer.de/lennart/projects/libdaemon"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "fd23eb5f6f986dcc7e708307355ba3289abe03cc381fc47a80bca4a50aa6b834"


@subpackage("libdaemon-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
