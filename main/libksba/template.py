pkgname = "libksba"
pkgver = "1.6.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "CMS and X.509 access library"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://gnupg.org/software/libksba/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "3f72c68db30971ebbf14367527719423f0a4d5f8103fc9f4a1c01a9fa440de5c"

@subpackage(f"libksba-devel")
def _devel(self):
   return self.default_devel()
