pkgname = "gpgme"
pkgver = "1.18.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gnupg"]
makedepends = ["libgpg-error-devel", "libassuan-devel", "glib-devel"]
depends = ["gnupg"]
pkgdesc = "GnuPG Made Easy"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "361d4eae47ce925dba0ea569af40e7b52c645c4ae2e65e5621bf1b6cdd8b0e9e"

@subpackage("gpgme-devel")
def _devel(self):
   return self.default_devel()
