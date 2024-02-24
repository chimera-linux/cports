pkgname = "libksba"
pkgver = "1.6.6"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "CMS and X.509 access library"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://gnupg.org/software/libksba/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "5dec033d211559338838c0c4957c73dfdc3ee86f73977d6279640c9cd08ce6a4"


@subpackage("libksba-devel")
def _devel(self):
    return self.default_devel()
