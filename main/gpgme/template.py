pkgname = "gpgme"
pkgver = "1.20.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gnupg"]
makedepends = ["libgpg-error-devel", "libassuan-devel", "glib-devel"]
depends = ["gnupg"]
pkgdesc = "GnuPG Made Easy"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "25a5785a5da356689001440926b94e967d02e13c49eb7743e35ef0cf22e42750"

@subpackage("gpgme-devel")
def _devel(self):
   return self.default_devel()

configure_gen = []
