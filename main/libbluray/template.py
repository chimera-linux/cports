pkgname = "libbluray"
pkgver = "1.3.3"
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
sha256 = "58ff52cdcee64c55dcc3c777a1c39fb41abd951b927978e4d2b6811b9193a488"

@subpackage("libbluray-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libbluray-progs")
def _progs(self):
    return self.default_progs()
