pkgname = "libassuan"
pkgver = "3.0.0"
pkgrel = 0
build_style = "gnu_configure"
# their autoconf is dumb
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "IPC library used by some GnuPG related software"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org/related_software/libassuan"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "0b160cbb898b852c6c04314b9a63e90ca87501305ad72a58a010f808665bbaf6"


@subpackage("libassuan-devel")
def _devel(self):
    return self.default_devel()
