pkgname = "libbluray"
pkgver = "1.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-optimizations", "--disable-bdjava-jar"]
hostmakedepends = ["pkgconf"]
makedepends = ["libxml2-devel", "fontconfig-devel"]
pkgdesc = "Library for Blu-Ray disk playback"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.videolan.org/developers/libbluray.html"
source = f"https://download.videolan.org/pub/videolan/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "e2dbaf99e84e0a9725f4985bcb85d41e52c2261cc651d8884b1b790b5ef016f9"

@subpackage("libbluray-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libbluray-progs")
def _progs(self):
    return self.default_progs()
