pkgname = "libdwarf"
pkgver = "2.3.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_DWARFGEN=ON",
    "-DBUILD_SHARED=ON",
    "-DDO_TESTING=ON",
    "-DPIC_ALWAYS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-ng-compat-devel", "zstd-devel"]
pkgdesc = "Library to access DWARF debugging information"
license = "LGPL-2.1-only AND GPL-2.0-only AND BSD-2-Clause AND BSD-3-Clause"
url = "https://www.prevanders.net/dwarf.html"
source = f"https://github.com/davea42/libdwarf-code/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7be0e6e17847b503317ed11ebf28668e6300b198cae3ec36cfe9126767c3be27"


def post_install(self):
    self.install_license("COPYING")
    self.install_license("src/bin/dwarfgen/COPYING", name="COPYING.dwarfgen")


@subpackage("libdwarf-devel")
def _(self):
    return self.default_devel()
