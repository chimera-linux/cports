pkgname = "opus"
pkgver = "1.6.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dcustom-modes=true",
    "-Ddeep-plc=enabled",
    "-Ddred=enabled",
    "-Dfloat-approx=true",
    "-Dosce=enabled",
    "-Dtests=enabled",
]
make_check_args = ["--timeout-multiplier", "10"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Totally open, royalty-free, highly versatile audio codec"
license = "BSD-3-Clause"
url = "https://www.opus-codec.org"
source = f"https://downloads.xiph.org/releases/opus/opus-{pkgver}.tar.gz"
sha256 = "6ffcb593207be92584df15b32466ed64bbec99109f007c82205f0194572411a1"


def post_install(self):
    self.install_license("COPYING")


@subpackage("opus-devel")
def _(self):
    return self.default_devel()
