pkgname = "gpgme"
# update contrib/gpgme-qt too
pkgver = "1.23.2"
pkgrel = 3
build_style = "gnu_configure"
# otherwise cmake files are broken
hostmakedepends = ["pkgconf", "gnupg", "automake", "libtool"]
makedepends = ["libgpg-error-devel", "libassuan-devel", "glib-devel"]
depends = ["gnupg"]
pkgdesc = "GnuPG Made Easy"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/gpgme/gpgme-{pkgver}.tar.bz2"
sha256 = "9499e8b1f33cccb6815527a1bc16049d35a6198a6c5fae0185f2bd561bce5224"


@subpackage("gpgme-devel")
def _(self):
    return self.default_devel()
