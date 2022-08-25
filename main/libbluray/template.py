pkgname = "libbluray"
pkgver = "1.3.2"
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
sha256 = "456814db9f07c1eecdef7e840fcbb20976ef814df875428bfb81ecf45851f170"

@subpackage("libbluray-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libbluray-progs")
def _progs(self):
    return self.default_progs()
