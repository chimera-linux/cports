pkgname = "opus"
pkgver = "1.5.2"
pkgrel = 2
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.opus-codec.org"
source = f"https://downloads.xiph.org/releases/opus/opus-{pkgver}.tar.gz"
sha256 = "65c1d2f78b9f2fb20082c38cbe47c951ad5839345876e46941612ee87f9a7ce1"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("opus-devel")
def _(self):
    return self.default_devel()
