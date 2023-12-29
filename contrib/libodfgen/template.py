pkgname = "libodfgen"
pkgver = "0.1.8"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["librevenge-devel", "boost-devel", "libxml2-devel"]
pkgdesc = "ODF generator for librevenge"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://sourceforge.net/p/libwpd/libodfgen"
source = f"$(SOURCEFORGE_SITE)/libwpd/{pkgname}/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "55200027fd46623b9bdddd38d275e7452d1b0ff8aeddcad6f9ae6dc25f610625"


@subpackage("libodfgen-devel")
def _devel(self):
    return self.default_devel()
