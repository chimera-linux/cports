pkgname = "libksba"
pkgver = "1.6.4"
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
sha256 = "bbb43f032b9164d86c781ffe42213a83bf4f2fee91455edfa4654521b8b03b6b"


@subpackage("libksba-devel")
def _devel(self):
    return self.default_devel()
