pkgname = "npth"
pkgver = "1.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "New portable threads library"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://gnupg.org/software/npth/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "1393abd9adcf0762d34798dc34fdcf4d0d22a8410721e76f1e3afcd1daa4e2d1"

@subpackage("npth-devel")
def _devel(self):
   return self.default_devel()
