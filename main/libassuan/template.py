pkgname = "libassuan"
pkgver = "2.5.6"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "IPC library used by some GnuPG related software"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org/related_software/libassuan"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "e9fd27218d5394904e4e39788f9b1742711c3e6b41689a31aa3380bd5aa4f426"


@subpackage("libassuan-devel")
def _devel(self):
    return self.default_devel()
