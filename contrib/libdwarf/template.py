pkgname = "libdwarf"
pkgver = "0.10.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    # checks for static/shared only and otherwise fails with =both
    "-Ddefault_library=shared",
    "-Ddwarfgen=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Parsing library for the DWARF file format"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-only AND GPL-2.0-only"
url = "https://www.prevanders.net/dwarf.html"
source = f"https://www.prevanders.net/libdwarf-{pkgver}.tar.xz"
sha256 = "b511a2dc78b98786064889deaa2c1bc48a0c70115c187900dd838474ded1cc19"


@subpackage("libdwarf-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libdwarf-devel")
def _devel(self):
    return self.default_devel()
