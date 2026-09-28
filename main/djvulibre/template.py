pkgname = "djvulibre"
pkgver = "3.5.29"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libtiff-devel", "libjpeg-turbo-devel"]
pkgdesc = "Utilities for the DjVu image format"
license = "GPL-2.0-or-later"
url = "http://djvu.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/djvu/djvulibre-{pkgver}.tar.gz"
sha256 = "d3b4b03ae2bdca8516a36ef6eb27b777f0528c9eda26745d9962824a3fdfeccf"


@subpackage("djvulibre-libs")
def _(self):
    self.renames = ["libdjvulibre"]

    return self.default_libs()


@subpackage("djvulibre-devel")
def _(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()
