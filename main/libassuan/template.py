pkgname = "libassuan"
pkgver = "2.5.7"
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
sha256 = "0103081ffc27838a2e50479153ca105e873d3d65d8a9593282e9c94c7e6afb76"


@subpackage("libassuan-devel")
def _devel(self):
    return self.default_devel()
