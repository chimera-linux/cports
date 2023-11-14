pkgname = "gpgme"
pkgver = "1.23.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gnupg", "automake", "libtool"]
makedepends = ["libgpg-error-devel", "libassuan-devel", "glib-devel"]
depends = ["gnupg"]
pkgdesc = "GnuPG Made Easy"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "a0c316f7ab7d3bfb01a8753c3370dc906e5b61436021f3b54ff1483b513769bd"


@subpackage("gpgme-devel")
def _devel(self):
    return self.default_devel()
