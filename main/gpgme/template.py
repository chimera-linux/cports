pkgname = "gpgme"
pkgver = "1.21.0"
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
sha256 = "416e174e165734d84806253f8c96bda2993fd07f258c3aad5f053a6efd463e88"


@subpackage("gpgme-devel")
def _devel(self):
    return self.default_devel()
