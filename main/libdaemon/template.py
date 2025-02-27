pkgname = "libdaemon"
pkgver = "0.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-lynx"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
pkgdesc = "Lightweight C library that eases the writing of UNIX daemons"
license = "LGPL-2.1-or-later"
url = "http://0pointer.de/lennart/projects/libdaemon"
source = f"{url}/libdaemon-{pkgver}.tar.gz"
sha256 = "fd23eb5f6f986dcc7e708307355ba3289abe03cc381fc47a80bca4a50aa6b834"


@subpackage("libdaemon-devel")
def _(self):
    return self.default_devel()
