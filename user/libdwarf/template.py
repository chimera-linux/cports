pkgname = "libdwarf"
pkgver = "2.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-ng-compat-devel", "zstd-devel"]
pkgdesc = "Library to access DWARF debugging information"
license = "LGPL-2.1-only AND GPL-2.0-only AND BSD-2-Clause AND BSD-3-Clause"
url = "https://www.prevanders.net/dwarf.html"
source = f"https://github.com/davea42/libdwarf-code/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0caec41d0a6294de5548273d7d47d7944a0d25b003b64b119bf2580c2ee49ad9"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libdwarf-devel")
def _(self):
    return self.default_devel()
