pkgname = "wavpack"
pkgver = "5.7.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "libtool", "pkgconf"]
pkgdesc = "Hybrid lossless audio compression"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.wavpack.com"
source = f"https://github.com/dbry/WavPack/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e81510fd9ec5f309f58d5de83e9af6c95e267a13753d7e0bbfe7b91273a88bee"


def post_install(self):
    self.install_license("COPYING")


@subpackage("wavpack-devel")
def _devel(self):
    return self.default_devel()


@subpackage("wavpack-progs")
def _progs(self):
    return self.default_progs()
