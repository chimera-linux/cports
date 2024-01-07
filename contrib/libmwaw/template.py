pkgname = "libmwaw"
pkgver = "0.3.22"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["librevenge-devel", "boost-devel", "zlib-devel"]
pkgdesc = "Library for importing legacy Mac documents"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://sourceforge.net/projects/libmwaw"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a1a39ffcea3ff2a7a7aae0c23877ddf4918b554bf82b0de5d7ce8e7f61ea8e32"


@subpackage("libmwaw-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libmwaw-devel")
def _devel(self):
    return self.default_devel()
