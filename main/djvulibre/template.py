pkgname = "djvulibre"
pkgver = "3.5.28"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "automake", "libtool"]
makedepends = ["libtiff-devel", "libjpeg-turbo-devel"]
pkgdesc = "Utilities for the DjVu image format"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://djvu.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/djvu/{pkgname}-{pkgver}.tar.gz"
sha256 = "fcd009ea7654fde5a83600eb80757bd3a76998e47d13c66b54c8db849f8f2edc"


@subpackage("libdjvulibre")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("djvulibre-devel")
def _devel(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()
