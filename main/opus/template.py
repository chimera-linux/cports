pkgname = "opus"
pkgver = "1.5.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dcustom-modes=true",
    "-Dfloat-approx=true",
    "-Dtests=enabled",
]
make_check_args = ["--timeout-multiplier", "10"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Totally open, royalty-free, highly versatile audio codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.opus-codec.org"
source = (
    f"https://downloads.xiph.org/releases/{pkgname}/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "b84610959b8d417b611aa12a22565e0a3732097c6389d19098d844543e340f85"
# FIXME int
hardening = ["vis", "cfi", "!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("opus-devel")
def _devel(self):
    return self.default_devel()
