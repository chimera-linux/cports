pkgname = "libedit"
_datever = "20210522"
_distver = 3.1
pkgver = f"{_datever}.{_distver}"
pkgrel = 0
build_style = "gnu_configure"
makedepends = ["ncurses-devel"]
pkgdesc = "Port of the NetBSD command line editing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.thrysoee.dk/editline"
sources = [f"http://thrysoee.dk/editline/{pkgname}-{_datever}-{_distver}.tar.gz"]
sha256 = ["0220bc2047e927c0c1984ef5f7b4eb2a9469a5b7bf12ba573ca3b23ca02bbb6f"]

options = ["bootstrap", "!check", "!lint"]

if not current.bootstrapping:
    hostmakedepends = ["pkgconf"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libedit-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"] + makedepends

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share/man/man3",
    ]
