pkgname = "libogg"
pkgver = "1.3.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Ogg bitstream file format library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.xiph.org/ogg"
source = f"https://downloads.xiph.org/releases/ogg/{pkgname}-{pkgver}.tar.xz"
sha256 = "c4d91be36fc8e54deae7575241e03f4211eb102afb3fc0775fbbc1b740016705"
# FIXME int
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libogg-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])


configure_gen = []
