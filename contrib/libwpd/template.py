pkgname = "libwpd"
pkgver = "0.10.3"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["librevenge-devel", "boost-devel"]
pkgdesc = "Library for importing WordPerfect documents"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://libwpd.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2465b0b662fdc5d4e3bebcdc9a79027713fb629ca2bff04a3c9251fdec42dd09"


@subpackage("libwpd-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libwpd-devel")
def _devel(self):
    return self.default_devel()
