pkgname = "npth"
pkgver = "1.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "New portable threads library"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://gnupg.org/software/npth/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "8589f56937b75ce33b28d312fccbf302b3b71ec3f3945fde6aaa74027914ad05"


@subpackage("npth-devel")
def _devel(self):
    return self.default_devel()
