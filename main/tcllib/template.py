pkgname = "tcllib"
pkgver = "2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "tcl"]
makedepends = ["tcl-devel"]
pkgdesc = "Tcl standard library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "TCL"
url = "https://core.tcl-lang.org/tcllib"
source = f"{url}/uv/tcllib-{pkgver}.tar.xz"
sha256 = "642c2c679c9017ab6fded03324e4ce9b5f4292473b62520e82aacebb63c0ce20"


def build(self):
    pass
