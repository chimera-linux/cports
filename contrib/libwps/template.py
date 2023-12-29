pkgname = "libwps"
pkgver = "0.4.14"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--disable-werror"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["librevenge-devel", "boost-devel"]
pkgdesc = "Library for importing Microsoft Works documents"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://sourceforge.net/p/libwps/wiki/Home"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "365b968e270e85a8469c6b160aa6af5619a4e6c995dbb04c1ecc1b4dd13e80de"


@subpackage("libwps-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libwps-devel")
def _devel(self):
    return self.default_devel()
