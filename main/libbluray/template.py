pkgname = "libbluray"
pkgver = "1.3.1"
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
sha256 = "c24b0f41c5b737bbb65c544fe63495637a771c10a519dfc802e769f112b43b75"

@subpackage("libbluray-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libbluray-progs")
def _progs(self):
    return self.default_progs()
